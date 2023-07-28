from io import BytesIO
from typing import Union
from pathlib import Path
from requests import Session
from subprocess import Popen
from shutil import copyfileobj
from os import PathLike, remove
from base64 import b64decode, b64encode
from requests.exceptions import ChunkedEncodingError

from tqdm import tqdm
from mpegdash.parser import MPEGDASHParser, MPEGDASH

from kinescope.kinescope import KinescopeVideo
from kinescope.const import KINESCOPE_BASE_URL
from kinescope.exceptions import *


class VideoDownloader:
    def __init__(self, kinescope_video: KinescopeVideo,
                 temp_dir: Union[str, PathLike] = './temp',
                 ffmpeg_path: Union[str, PathLike] = None,
                 mp4decrypt_path: Union[str, PathLike] = None):
        self.kinescope_video: KinescopeVideo = kinescope_video

        self.temp_path: Path = Path(temp_dir)
        self.temp_path.mkdir(parents=True, exist_ok=True)

        self.ffmpeg_path = ffmpeg_path
        self.mp4decrypt_path = mp4decrypt_path

        self.http = Session()

        self.mpd_master: MPEGDASH = self._fetch_mpd_master()

    def __del__(self):
        for filename in self.temp_path.glob('*.mp4'):
            remove(filename)
        for filename in self.temp_path.glob('*.mp4.enc'):
            remove(filename)

    def _merge_tracks(self, source_video_filepath: Union[str, PathLike],
                      source_audio_filepath: Union[str, PathLike],
                      target_filepath: Union[str, PathLike]):
        try:
            Popen(f"{self.ffmpeg_path if self.ffmpeg_path else 'ffmpeg'} "
                  f"-i {source_video_filepath} "
                  f"-i {source_audio_filepath} "
                  f"-c copy {target_filepath} "
                  f"-y -loglevel error").communicate()
        except FileNotFoundError:
            raise FFmpegNotFoundError('FFmpeg binary was not found at the specified path')

    def _decrypt_video(self, source_filepath: Union[str, PathLike],
                       target_filepath: Union[str, PathLike],
                       key: str):
        try:
            Popen(f"{self.mp4decrypt_path if self.mp4decrypt_path else 'mp4decrypt'} "
                  f"--key 1:{key} "
                  f"\"{source_filepath}\" "
                  f"\"{target_filepath}\"").communicate()
        except FileNotFoundError:
            raise FFmpegNotFoundError('mp4decrypt binary was not found at the specified path')

    def _get_license_key(self) -> str:
        return b64decode(
            self.http.post(
                url=self.kinescope_video.get_clearkey_license_url(),
                headers={'origin': KINESCOPE_BASE_URL},
                json={
                    'kids': [
                        b64encode(bytes.fromhex(
                            self.mpd_master
                            .periods[0]
                            .adaptation_sets[0]
                            .content_protections[0]
                            .cenc_default_kid.replace('-', '')
                        )).decode().replace('=', '')
                    ],
                    'type': 'temporary'
                }
            ).json()['keys'][0]['k'] + '=='
        ).hex() if self.mpd_master.periods[0].adaptation_sets[0].content_protections else None

    def _fetch_segment(self,
                       segment_url: str,
                       file):
        for _ in range(5):
            try:
                copyfileobj(
                    BytesIO(self.http.get(segment_url, stream=True).content),
                    file
                )
                return
            except ChunkedEncodingError:
                pass

        raise SegmentDownloadError(f'Failed to download segment {segment_url}')

    def _fetch_segments(self,
                        segments_urls: list[str],
                        filepath: Union[str, PathLike],
                        progress_bar_label: str = ''):
        segments_urls = [seg for i, seg in enumerate(segments_urls) if i == segments_urls.index(seg)]
        with open(filepath, 'wb') as f:
            with tqdm(desc=progress_bar_label,
                      total=len(segments_urls),
                      bar_format='{desc}: {percentage:3.0f}%|{bar:10}| [{n_fmt}/{total_fmt}]') as progress_bar:
                for segment_url in segments_urls:
                    self._fetch_segment(segment_url, f)
                    progress_bar.update()

    def _get_segments_urls(self, resolution: tuple[int, int]) -> dict[str:list[str]]:
        try:
            return {
                adaptation_set.mime_type: [
                    segment_url.media for segment_url in adaptation_set.representations[
                        [(r.width, r.height) for r in adaptation_set.representations].index(resolution)
                        if adaptation_set.representations[0].height else 0
                    ].segment_lists[0].segment_urls
                ] for adaptation_set in self.mpd_master.periods[0].adaptation_sets
            }
        except ValueError:
            raise InvalidResolution('Invalid resolution specified')

    def _fetch_mpd_master(self) -> MPEGDASH:
        return MPEGDASHParser.parse(self.http.get(
            url=self.kinescope_video.get_mpd_master_playlist_url(),
            headers={'Referer': KINESCOPE_BASE_URL}
        ).text)

    def get_resolutions(self) -> list[tuple[int, int]]:
        for adaptation_set in self.mpd_master.periods[0].adaptation_sets:
            if adaptation_set.representations[0].height:
                return [(r.width, r.height) for r in sorted(adaptation_set.representations, key=lambda r: r.height)]

    def download(self, filepath: str, resolution: tuple[int, int] = None):
        if not resolution:
            resolution = self.get_resolutions()[-1]

        key = self._get_license_key()

        self._fetch_segments(
            self._get_segments_urls(resolution)['video/mp4'],
            self.temp_path / f'{self.kinescope_video.video_id.replace("-", "")}_video.mp4{".enc" if key else ""}',
            'Video'
        )
        self._fetch_segments(
            self._get_segments_urls(resolution)['audio/mp4'],
            self.temp_path / f'{self.kinescope_video.video_id.replace("-", "")}_audio.mp4{".enc" if key else ""}',
            'Audio'
        )

        if key:
            print('[*] Decrypting...', end=' ')
            self._decrypt_video(
                self.temp_path / f'{self.kinescope_video.video_id.replace("-", "")}_video.mp4.enc',
                self.temp_path / f'{self.kinescope_video.video_id.replace("-", "")}_video.mp4',
                key
            )
            self._decrypt_video(
                self.temp_path / f'{self.kinescope_video.video_id.replace("-", "")}_audio.mp4.enc',
                self.temp_path / f'{self.kinescope_video.video_id.replace("-", "")}_audio.mp4',
                key
            )
            print('Done')

        filepath = Path(filepath).with_suffix('.mp4')
        filepath.parent.mkdir(parents=True, exist_ok=True)

        print('[*] Merging tracks...', end=' ')
        self._merge_tracks(
            self.temp_path / f'{self.kinescope_video.video_id.replace("-", "")}_video.mp4',
            self.temp_path / f'{self.kinescope_video.video_id.replace("-", "")}_audio.mp4',
            filepath
        )
        print('Done')
