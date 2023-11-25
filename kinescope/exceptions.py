class UrlOrVideoIdRequired(Exception):
    pass


class VideoNotFound(Exception):
    pass


class AccessDenied(Exception):
    pass


class InvalidResolution(Exception):
    pass


class DownloadError(Exception):
    pass


class SegmentDownloadError(DownloadError):
    pass


class FFmpegNotFoundError(FileNotFoundError):
    pass


class Mp4DecryptNotFoundError(FileNotFoundError):
    pass


class UnsupportedEncryption(Exception):
    pass
