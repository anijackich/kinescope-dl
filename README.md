# kinescope-dl
Video downloader for [kinescope.io](https://kinescope.io)

## Installation
[Download](https://github.com/anijackich/kinescope-dl/archive/refs/heads/master.zip) and unpack the script or clone it:
```commandline
git clone https://github.com/anijackich/kinescope-dl.git
```
[FFmpeg](https://ffmpeg.org/download.html) and [mp4decrypt](https://www.bento4.com/downloads/) binaries should be in the same directory as the project.

<details>
<summary>Use a virtual environment (optional)</summary>

```commandline
python -m venv venv
```
On Windows, run:
```commandline
venv\Scripts\activate.bat
```
On Unix or MacOS, run:
```commandline
source venv/bin/activate
```
</details>
 
Install the requirements:
```commandline
pip install -r requirements.txt
```

## Usage
```commandline
python kinescope-dl.py
```
```
> KINESCOPE URL or VIDEO ID: https://kinescope.io/123456789
> REFERER URL (optional): https://example.com
1) 360p
2) 480p
3) 720p
4) 1080p
> QUALITY: 4
```
KINESCOPE URL — url of the video on Kinescope (e.g. ```https://kinescope.io/123456789```)

VIDEO ID — id of the video, REFERER URL will not be asked if you specify it (e.g. ```1a2b3c4d-5e6f-7g8h-9i10-11j12k13l14m```)

REFERER URL — url of the site where the video is embedded (e.g. ```https://example.com```)
```
= DOWNLOADING =================
Video: 100%|██████████| [10/10]
Audio: 100%|██████████| [4/4]
===============================
```
Videos will be saved in this directory. 