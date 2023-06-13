# kinescope-dl
Video downloader for [kinescope.io](https://kinescope.io)

## Installation
[Download](https://github.com/anijackich/kinescope-dl/archive/refs/heads/master.zip) and unpack the script or clone it:
```commandline
git clone https://github.com/anijackich/kinescope-dl.git
```
[FFmpeg](https://ffmpeg.org/download.html) and [mp4decrypt](https://www.bento4.com/downloads/) should be in the same directory as the project.

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

= DOWNLOADING ================
Video: 100%|██████████| [10/10]
Audio: 100%|██████████| [4/4]
==============================
```
Videos will be saved in this directory. 