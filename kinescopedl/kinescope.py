import typer
import requests
import logging

from typing import Optional
from kinescopedl.const import (
    KINESCOPE_MASTER_PLAYLIST_URL,
    KINESCOPE_CLEARKEY_LICENSE_URL,
)

_logger = logging.getLogger("kinescopedl")


class KinescopeVideo:
    def __init__(
        self,
        url: str,
        referer_url: Optional[str] = None,
    ):
        self.url = url
        self.referer_url = referer_url
        self.http = requests.Session()
        self.__video_id = self.__get_video_id()

    @property
    def video_id(self) -> str:
        return self.__video_id

    @property
    def mpd_master_playlist_url(self) -> str:
        return KINESCOPE_MASTER_PLAYLIST_URL.format(video_id=self.__video_id)

    @property
    def clearkey_license_url(self) -> str:
        return KINESCOPE_CLEARKEY_LICENSE_URL.format(video_id=self.__video_id)

    def __get_video_id(self):
        try:
            r = self.http.get(url=self.url, headers={"Referer": self.referer_url})
        except requests.exceptions.ConnectionError:
            _logger.error("Connection error")
            raise typer.Abort()
        except requests.exceptions.InvalidURL:
            _logger.error("Invalid URL")
            raise typer.Abort()
        except requests.exceptions.MissingSchema:
            _logger.error("Missing schema")
            raise typer.Abort()
        except requests.exceptions.InvalidSchema:
            _logger.error("Invalid schema")
            raise typer.Abort()

        if r.status_code == 404:
            _logger.error("Video not found")
            raise typer.Abort()
        if 'id: "' not in r.text:
            _logger.error("Access to the video is denied. Wrong referer_url is specified?")
            raise typer.Abort()

        return r.text.split('id: "')[1].split('"')[0]
