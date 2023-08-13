# kinescope-dl
![https://kinescope.io](https://img.shields.io/badge/Kinescope-fe681d.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB3aWR0aD0iMTAwJSIgdmlld0JveD0iMCAwIDI0MCAyNDAiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0MCAyNDAiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8cGF0aCBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTA5Ljk2MjQwMiwxNDEuMTU5Njk4IAoJQzEyNi44ODM4MTIsMTY5LjY1MzcwMiAxMTEuMjAxOTA0LDIwMi4zNDk1MDMgNzguNzI4NTAwLDIwNS44OTgzMTUgCglDNTkuMjQ1NDM4LDIwOC4wMjc0OTYgMzkuMzc1NDM1LDE5NC45NTcyOTEgMzQuODI5MjI3LDE3My4xMDI5MDUgCglDMzAuNjQ2ODA5LDE1Mi45OTczMTQgNDAuNDg0MDQ3LDEzNC4zODc0MzYgNTkuMjk1MjQ2LDEyNi4xMjgwMTQgCglDNzcuMTY4NjU1LDExOC4yODAzNDIgOTcuNDE3ODQ3LDEyNC4xOTE0NTIgMTA5Ljk2MjQwMiwxNDEuMTU5Njk4IAp6Ii8+CjxwYXRoIGZpbGw9IiMwMDAwMDAiIG9wYWNpdHk9IjEuMDAwMDAwIiBzdHJva2U9Im5vbmUiIAoJZD0iCk00Ni4zMDA0NzYsNDguMjg4NTUxIAoJQzU0Ljg3NDA2Miw0MC4zNzA3NDMgNjQuOTQ1Mzg5LDM1LjU2ODYwMCA3NS45Nzc0MDksMzYuMjA4NDg4IAoJQzk2LjgyOTE4NSwzNy40MTc5NDIgMTEyLjU5MTY3NSw1MC40NTM2MjUgMTE2LjI3MzE0OCw3MC43NzQxMzkgCglDMTIwLjM4MTIyNiw5My40NDkzMjYgMTA1LjcxOTQwNiwxMTUuMjExNDY0IDgzLjI5MTIyMiwxMTguOTUxMDczIAoJQzU3LjQ2Nzk1NywxMjMuMjU2NzY3IDM4LjYzODg3NCwxMDYuMzM3NDAyIDM0LjU3MjE4OSw4NS44MTQ3MDUgCglDMzEuNjU3NjU4LDcxLjEwNjM5MiAzNi42MzUwMTQsNTkuMjQwNDYzIDQ2LjMwMDQ3Niw0OC4yODg1NTEgCnoiLz4KPHBhdGggZmlsbD0iIzAwMDAwMCIgb3BhY2l0eT0iMS4wMDAwMDAiIHN0cm9rZT0ibm9uZSIgCglkPSIKTTE0MC41MjU4NjQsNDIuMzkyMTk3IAoJQzE2OC45NzQyMTMsMjYuMDM1MDE3IDIwMy44Mzc5NTIsNDUuOTU0NDE0IDIwMy4zMjE2NTUsNzkuMDkzNjIwIAoJQzIwMy4wMDM5MjIsOTkuNDg3ODU0IDE4NS45MTcwNTMsMTE3LjkzMzIwNSAxNjYuNzExMTA1LDExOS40MTE1MTQgCglDMTM5LjM0ODc3MCwxMjEuNTE3NjQ3IDEyMi45MDc3OTksMTAyLjMwOTU2MyAxMjAuNzQ5MTY4LDgzLjgzOTY5OSAKCUMxMTguNjgyMDMwLDY2LjE1MjU5NiAxMjUuMTA0MTQ5LDUyLjI3NDQwMyAxNDAuNTI1ODY0LDQyLjM5MjE5NyAKeiIvPgo8cGF0aCBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTQ5Ljk3MTc3MSwxMjMuNzI0MTkwIAoJQzE1OS4xOTI0MTMsMTIxLjk5MDI5NSAxNjQuMjA3NjU3LDEyNi4xNjU0NzQgMTY5LjExMjU2NCwxMzMuMjExNjU1IAoJQzE4NC41Mjc2MTgsMTU1LjM1NjM1NCAyMDAuNzY2NDM0LDE3Ni45MjczOTkgMjE2LjY2MTQ1MywxOTguNzM4NjYzIAoJQzIxNy44MDI3MzQsMjAwLjMwNDcxOCAyMTkuMzc4NzA4LDIwMS42ODMzMzQgMjE5LjUxNDgxNiwyMDMuNzY0NjAzIAoJQzIxOC4wMjk3MjQsMjA1LjY4MTU2NCAyMTYuMDQxNzMzLDIwNS4wNjQ3NTggMjE0LjMxNTAwMiwyMDUuMDcwMjM2IAoJQzE5OC4xNTIxMTUsMjA1LjEyMTY0MyAxODEuOTg4NjkzLDIwNS4wNDQ5MjIgMTY1LjgyNjE1NywyMDUuMTM1NzczIAoJQzE2Mi44NzQyOTgsMjA1LjE1MjM3NCAxNjAuNzg1NTgzLDIwNC4xOTkxODggMTU5LjA1MDk2NCwyMDEuODExODEzIAoJQzE0MS4yMjc5MzYsMTc3LjI4MTk5OCAxMjMuMzUxMTgxLDE1Mi43OTEyMjkgMTA1LjQ5MzI0OCwxMjguMjg2Nzc0IAoJQzEwNC44MTE4NTIsMTI3LjM1MTc2OCAxMDQuMDI4MzUxLDEyNi40NTE3NjcgMTA0LjE1MzY1NiwxMjMuNzI0NjYzIAoJQzExOS4xOTUxMDcsMTIzLjcyNDY2MyAxMzQuMzM2MzgwLDEyMy43MjQ2NjMgMTQ5Ljk3MTc3MSwxMjMuNzI0MTkwIAp6Ii8+Cjwvc3ZnPg==)
![https://t.me/KinescopeDL](https://img.shields.io/badge/Join-Telegram_Chat-blue?logo=telegram)
![https://github.com/anijackich/kinescope-dl/blob/master/LICENSE](https://img.shields.io/github/license/anijackich/kinescope-dl)
![https://github.com/anijackich/kinescope-dl/releases/latest](https://img.shields.io/github/v/release/anijackich/kinescope-dl)
![](https://img.shields.io/github/downloads/anijackich/kinescope-dl/latest/total)
![](https://global-uploads.webflow.com/605c72811fff3764f0148463/60c8b0e2026e8442e92a76c8_prod.png)

kinescope-dl is a video downloader for [Kinescope.io](https://kinescope.io)

## 🔗 Requirements
[FFmpeg](https://ffmpeg.org/download.html) and [mp4decrypt](https://www.bento4.com/downloads/) binaries should be in the same directory as the project or paths to them should be passed when running the command.

## 🔨 Installation
Download and unpack the [latest release](https://github.com/anijackich/kinescope-dl/releases/latest) for your OS.



## 🚀 Usage
```commandline
kinescope-dl [OPTIONS] SOURCE OUTPUT
```
SOURCE — url or ```videoId``` of the video on Kinescope 
(e.g. ```https://kinescope.io/123456789``` or ```123e4567-e89b-12d3-a456-426655440000```)

OUTPUT — path to the output mp4 file (e.g. ```./video.mp4```)

## ⚙️ Options
```
--help                 Show this message and exit
-r, --referer TEXT     Referer url of the site where the video is embedded
--best-quality         Automatically select the best possible quality
--ffmpeg-bin PATH      Path to FFmpeg binary
--mp4decrypt-bin PATH  Path to mp4decrypt binary
--temp PATH            Path to directory for temporary files
```

Referer URL — url of the site where the video is embedded (e.g. ```https://example.com```)
### Example
```commandline
python kinescope-dl.py -r https://example.com --best-quality https://kinescope.io/123456789 ./videos/video.mp4
```
