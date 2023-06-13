import requests
from os import remove
from io import BytesIO
from subprocess import Popen
from shutil import copyfileobj
from base64 import b64encode, b64decode

from tqdm import tqdm
from mpegdash.parser import MPEGDASHParser

TMP_VIDEO_PATH = 'video.mp4'
TMP_AUDIO_PATH = 'audio.mp4'

KINESCOPE_BASE_URL = 'https://kinescope.io'
KINESCOPE_MASTER_URL = KINESCOPE_BASE_URL + '/{video_id}/master.mpd'
KINESCOPE_CLEARKEY_LICENSE_URL = 'https://license.kinescope.io/v1/vod/{video_id}/acquire/clearkey?token='

kinescope_id = input('> KINESCOPE URL or VIDEO ID: ').replace(KINESCOPE_BASE_URL, '').replace('/', '')

kinescope_video_id = requests.get(
    url=KINESCOPE_BASE_URL + '/' + kinescope_id,
    headers={'Referer': input('> REFERER URL (optional): ')}
).text.split('id: "')[1].split('"')[0] if kinescope_id.isdigit() else kinescope_id

master = MPEGDASHParser.parse(requests.get(
    url=KINESCOPE_MASTER_URL.format(video_id=kinescope_video_id),
    headers={'Referer': KINESCOPE_BASE_URL}
).text)

segments_urls = {
    adaptation_set.mime_type: [
        segment_url.media for segment_url in sorted(
            adaptation_set.representations,
            key=lambda x: x.height
        )[
            int(input('\n'.join([
                f'{i + 1}) {r.height}p' for i, r in enumerate(
                    sorted(adaptation_set.representations, key=lambda x: x.height)
                )
            ]) + '\n> QUALITY: ')) - 1
            if adaptation_set.representations[0].height else 0
        ].segment_lists[0].segment_urls
    ] for adaptation_set in master.periods[0].adaptation_sets
}

key = b64decode(requests.post(
    url=KINESCOPE_CLEARKEY_LICENSE_URL.format(video_id=kinescope_video_id),
    headers={'origin': KINESCOPE_BASE_URL},
    json={
        'kids': [
            b64encode(bytes.fromhex(
                master.periods[0].adaptation_sets[0].content_protections[0].cenc_default_kid.replace('-', '')
            )).decode().replace('=', '')
        ],
        'type': 'temporary'
    }
).json()['keys'][0]['k'] + '==').hex() if master.periods[0].adaptation_sets[0].content_protections else None

session = requests.Session()

print('\n= DOWNLOADING ================')
for track in [
    ['Video', TMP_VIDEO_PATH + ('.enc' if key else ''), segments_urls['video/mp4']],
    ['Audio', TMP_AUDIO_PATH + ('.enc' if key else ''), segments_urls['audio/mp4']]
]:
    with open(track[1], 'wb') as f:
        segments = [seg for i, seg in enumerate(track[2]) if i == track[2].index(seg)]
        with tqdm(desc=track[0],
                  total=len(segments),
                  bar_format='{desc}: {percentage:3.0f}%|{bar}| [{n_fmt}/{total_fmt}]') as progress_bar:
            for segment_url in segments:
                while True:
                    try:
                        copyfileobj(BytesIO(session.get(segment_url, stream=True).content), f)
                        break
                    except requests.exceptions.ChunkedEncodingError:
                        pass
                progress_bar.update()

    if key:
        Popen(f"mp4decrypt --key 1:{key} \"{track[1]}\" \"{track[1][:-4]}\"").communicate()
        remove(track[1])

print('==============================')

Popen(f"ffmpeg -i video.mp4 -i audio.mp4 -c copy {kinescope_video_id}.mp4 -y -loglevel error").communicate()
remove(TMP_VIDEO_PATH)
remove(TMP_AUDIO_PATH)
