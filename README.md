# kinescope-dl
Video downloader for [kinescope.io](https://kinescope.io)

## 🔗 Requirements
[FFmpeg](https://ffmpeg.org/download.html) and [mp4decrypt](https://www.bento4.com/downloads/) binaries should be in the same directory as the project or paths to them should be passed when running the command.


## 🔨 Installation
[Download](https://github.com/anijackich/kinescope-dl/archive/refs/heads/master.zip) and unpack the script or clone it:
```commandline
git clone https://github.com/anijackich/kinescope-dl.git
```

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

## 🚀 Usage
```commandline
python kinescope-dl.py [OPTIONS] SOURCE OUTPUT
```
### Options
```
--help                 Show this message and exit
-r, --referer TEXT     Referer url of the site where the video is embedded
--best-quality         Automatically select the best possible quality
--ffmpeg-bin PATH      Path to FFmpeg binary
--mp4decrypt-bin PATH  Path to mp4decrypt binary
--temp PATH            Path to directory for temporary files
```
Video URL — url of the video on Kinescope (e.g. ```https://kinescope.io/123456789```)

Video Id — id of the video; when specifying it, referer url is not needed (e.g. ```1a2b3c4d-5e6f-7g8h-9i10-11j12k13l14m```)

Referer URL — url of the site where the video is embedded (e.g. ```https://example.com```)
### Example
```commandline
python kinescope-dl.py -r https://example.com --best-quality https://kinescope.io/123456789 ./videos/video.mp4
```