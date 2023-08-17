# Kinescope-dl
[![Kinescope](https://img.shields.io/badge/Kinescope-fe681d.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB3aWR0aD0iMTAwJSIgdmlld0JveD0iMCAwIDI0MCAyNDAiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0MCAyNDAiIHhtbDpzcGFjZT0icHJlc2VydmUiPgo8cGF0aCBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTA5Ljk2MjQwMiwxNDEuMTU5Njk4IAoJQzEyNi44ODM4MTIsMTY5LjY1MzcwMiAxMTEuMjAxOTA0LDIwMi4zNDk1MDMgNzguNzI4NTAwLDIwNS44OTgzMTUgCglDNTkuMjQ1NDM4LDIwOC4wMjc0OTYgMzkuMzc1NDM1LDE5NC45NTcyOTEgMzQuODI5MjI3LDE3My4xMDI5MDUgCglDMzAuNjQ2ODA5LDE1Mi45OTczMTQgNDAuNDg0MDQ3LDEzNC4zODc0MzYgNTkuMjk1MjQ2LDEyNi4xMjgwMTQgCglDNzcuMTY4NjU1LDExOC4yODAzNDIgOTcuNDE3ODQ3LDEyNC4xOTE0NTIgMTA5Ljk2MjQwMiwxNDEuMTU5Njk4IAp6Ii8+CjxwYXRoIGZpbGw9IiMwMDAwMDAiIG9wYWNpdHk9IjEuMDAwMDAwIiBzdHJva2U9Im5vbmUiIAoJZD0iCk00Ni4zMDA0NzYsNDguMjg4NTUxIAoJQzU0Ljg3NDA2Miw0MC4zNzA3NDMgNjQuOTQ1Mzg5LDM1LjU2ODYwMCA3NS45Nzc0MDksMzYuMjA4NDg4IAoJQzk2LjgyOTE4NSwzNy40MTc5NDIgMTEyLjU5MTY3NSw1MC40NTM2MjUgMTE2LjI3MzE0OCw3MC43NzQxMzkgCglDMTIwLjM4MTIyNiw5My40NDkzMjYgMTA1LjcxOTQwNiwxMTUuMjExNDY0IDgzLjI5MTIyMiwxMTguOTUxMDczIAoJQzU3LjQ2Nzk1NywxMjMuMjU2NzY3IDM4LjYzODg3NCwxMDYuMzM3NDAyIDM0LjU3MjE4OSw4NS44MTQ3MDUgCglDMzEuNjU3NjU4LDcxLjEwNjM5MiAzNi42MzUwMTQsNTkuMjQwNDYzIDQ2LjMwMDQ3Niw0OC4yODg1NTEgCnoiLz4KPHBhdGggZmlsbD0iIzAwMDAwMCIgb3BhY2l0eT0iMS4wMDAwMDAiIHN0cm9rZT0ibm9uZSIgCglkPSIKTTE0MC41MjU4NjQsNDIuMzkyMTk3IAoJQzE2OC45NzQyMTMsMjYuMDM1MDE3IDIwMy44Mzc5NTIsNDUuOTU0NDE0IDIwMy4zMjE2NTUsNzkuMDkzNjIwIAoJQzIwMy4wMDM5MjIsOTkuNDg3ODU0IDE4NS45MTcwNTMsMTE3LjkzMzIwNSAxNjYuNzExMTA1LDExOS40MTE1MTQgCglDMTM5LjM0ODc3MCwxMjEuNTE3NjQ3IDEyMi45MDc3OTksMTAyLjMwOTU2MyAxMjAuNzQ5MTY4LDgzLjgzOTY5OSAKCUMxMTguNjgyMDMwLDY2LjE1MjU5NiAxMjUuMTA0MTQ5LDUyLjI3NDQwMyAxNDAuNTI1ODY0LDQyLjM5MjE5NyAKeiIvPgo8cGF0aCBmaWxsPSIjMDAwMDAwIiBvcGFjaXR5PSIxLjAwMDAwMCIgc3Ryb2tlPSJub25lIiAKCWQ9IgpNMTQ5Ljk3MTc3MSwxMjMuNzI0MTkwIAoJQzE1OS4xOTI0MTMsMTIxLjk5MDI5NSAxNjQuMjA3NjU3LDEyNi4xNjU0NzQgMTY5LjExMjU2NCwxMzMuMjExNjU1IAoJQzE4NC41Mjc2MTgsMTU1LjM1NjM1NCAyMDAuNzY2NDM0LDE3Ni45MjczOTkgMjE2LjY2MTQ1MywxOTguNzM4NjYzIAoJQzIxNy44MDI3MzQsMjAwLjMwNDcxOCAyMTkuMzc4NzA4LDIwMS42ODMzMzQgMjE5LjUxNDgxNiwyMDMuNzY0NjAzIAoJQzIxOC4wMjk3MjQsMjA1LjY4MTU2NCAyMTYuMDQxNzMzLDIwNS4wNjQ3NTggMjE0LjMxNTAwMiwyMDUuMDcwMjM2IAoJQzE5OC4xNTIxMTUsMjA1LjEyMTY0MyAxODEuOTg4NjkzLDIwNS4wNDQ5MjIgMTY1LjgyNjE1NywyMDUuMTM1NzczIAoJQzE2Mi44NzQyOTgsMjA1LjE1MjM3NCAxNjAuNzg1NTgzLDIwNC4xOTkxODggMTU5LjA1MDk2NCwyMDEuODExODEzIAoJQzE0MS4yMjc5MzYsMTc3LjI4MTk5OCAxMjMuMzUxMTgxLDE1Mi43OTEyMjkgMTA1LjQ5MzI0OCwxMjguMjg2Nzc0IAoJQzEwNC44MTE4NTIsMTI3LjM1MTc2OCAxMDQuMDI4MzUxLDEyNi40NTE3NjcgMTA0LjE1MzY1NiwxMjMuNzI0NjYzIAoJQzExOS4xOTUxMDcsMTIzLjcyNDY2MyAxMzQuMzM2MzgwLDEyMy43MjQ2NjMgMTQ5Ljk3MTc3MSwxMjMuNzI0MTkwIAp6Ii8+Cjwvc3ZnPg==)](https://kinescope.io)
[![https://t.me/KinescopeDL](https://img.shields.io/badge/Join-Telegram_Chat-blue?logo=telegram)](https://t.me/KinescopeDL)
[![License: Unlicense](https://img.shields.io/github/license/anijackich/kinescope-dl)](https://github.com/anijackich/kinescope-dl/blob/master/LICENSE)
[![Release](https://img.shields.io/github/v/release/anijackich/kinescope-dl)](https://github.com/anijackich/kinescope-dl/releases/latest)
![Downloads](https://img.shields.io/github/downloads/anijackich/kinescope-dl/latest/total)

![](https://i.imgur.com/DU9rSdx.png)

Kinescope-dl is a fast video downloader for [Kinescope](https://kinescope.io) player with encrypted videos support.

---
Easily download videos with one command
```shell
kinescope-dl https://kinescope.io/123456789 output.mp4
```
---
Join our [community chat](https://t.me/KinescopeDL) in Telegram to discuss issues or if you need help.

## ⬇️ Installation
Download and unpack the [latest release](https://github.com/anijackich/kinescope-dl/releases/latest) for your OS.

Windows users can place .exe file in any location on their [PATH](https://en.wikipedia.org/wiki/PATH_%28variable%29) or just call script as `./path/to/executable/kinescope-dl.exe`

For UNIX users (Linux, macOS, etc.):
```shell
sudo mv ./path/to/executable/kinescope-dl /usr/local/bin/kinescope-dl
sudo chmod a+rx /usr/local/bin/kinescope-dl
```

## 🚀 Usage
```commandline
kinescope-dl [OPTIONS] INPUT_URL OUTPUT_FILE
```
INPUT_URL — url of the video on Kinescope  
OUTPUT_FILE — path to the output mp4 file

### Options
      -r, --referer URL      Referer url of the site where the video is embedded
      --best-quality         Automatically select the best possible quality
      --temp PATH            Path to directory for temporary files
      --help                 Show this message and exit

### Example
```shell
kinescope-dl -r https://example.com --best-quality https://kinescope.io/123456789 ./my_videos/video.mp4
```

## 🔨 Build from sources
### Requirements
[FFmpeg](https://ffmpeg.org/download.html) and [mp4decrypt](https://www.bento4.com/downloads/) are required.

### Building
1. Download and install the latest version of [Python 3](https://www.python.org/downloads/)
2. Ensure that you have pip installed:
    ```shell
    python -m ensurepip --upgrade
    ```
3. Clone the project using [git](https://git-scm.com/downloads):
    ```shell
    git clone https://github.com/anijackich/kinescope-dl.git
    ```
    or directly download and unpack the [source code](https://github.com/anijackich/kinescope-dl/archive/refs/heads/master.zip).
4. Open console in the project directory
5. Install and use virtualenv (optional):
    ```shell
    pip install virtualenv
    python3 -m venv venv
    ```
    On Windows, run:
    ```shell
    .\venv\Scripts\activate.bat
    ```
    On Unix or MacOS, run:
    ```shell
    source venv/bin/activate
    ```
6. Install requirements:
    ```shell
    pip install -r requirements.txt
    ```
7. Install PyInstaller:
    ```shell
    pip install pyinstaller
    ```
8. Set environment variables with FFmpeg and mp4decrypt binaries paths:

   On Windows, run: 
   ```shell
   set FFMPEG_PATH=C:\path\to\ffmpeg.exe
   set MP4DECRYPT_PATH=C:\path\to\mp4decrypt.exe
   ```
   On Unix or MacOS, run:
   ```shell
   export FFMPEG_PATH=/path/to/ffmpeg
   export MP4DECRYPT_PATH=/path/to/mp4decrypt
   ```
9. Build the project:
    ```shell
    pyinstaller kinescope-dl.spec
    ```
10. Bundled script should be available in the _dist_ folder