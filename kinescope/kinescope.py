from requests import Session
from typing import Optional

from kinescope.const import *
from kinescope.exceptions import *


class KinescopeVideo:
    def __init__(self, url: Optional[str] = None,
                 video_id: Optional[str] = None,
                 referer_url: Optional[str] = None):
        if not (url or video_id):
            raise UrlOrVideoIdRequired('URL or Video Id is required')

        self.url = url
        self.video_id = video_id
        self.referer_url = referer_url

        self.http = Session()

        if not self.video_id:
          if "mpd" in self.url:
            self.video_id = self._get_video_id_from_mpd()
          else:
            self.video_id = self._get_video_id()

    def _get_video_id_from_mpd(self):
        print("Video ID FOUND:")
        videoId = self.url.split("https://kinescope.io/")[1].split("/")[0]
        print(videoId)

        return videoId

    def _get_video_id(self):
        r = self.http.get(
            url=self.url,
            headers={'Referer': self.referer_url}
        )

        if r.status_code == 404:
            raise VideoNotFound('Video not found')

        if 'id: "' not in r.text:
            raise AccessDenied('Access to the video is denied. Wrong referer_url is specified?')

        return r.text.split('id: "')[1].split('"')[0]

    def get_mpd_master_playlist_url(self) -> str:
        if "mpd" in self.url:
          return self.url
        else:
          return KINESCOPE_MASTER_PLAYLIST_URL.format(video_id=self.video_id)

    def get_clearkey_license_url(self) -> str:
        return KINESCOPE_CLEARKEY_LICENSE_URL.format(video_id=self.video_id)
