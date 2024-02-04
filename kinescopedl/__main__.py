import typer

from pathlib import Path
from urllib.parse import urlparse

from rich.console import Console
from kinescopedl import KinescopeVideo, KinescopeDownloader
from kinescopedl.di import app_container

app = app_container.typer_app
console = app_container.console


def parse_url(value: str) -> str:
    try:
        parsed_url = urlparse(value)
        if parsed_url.scheme and parsed_url.netloc:
            return value
        else:
            raise typer.BadParameter(f"Expected valid url. Got {value}")
    except Exception as E:
        raise typer.BadParameter(f"Expected valid url. Got {value}: {E}")


def callback_output_file(value: Path) -> Path:
    value = value.resolve()
    if value.exists():
        confirm = typer.confirm(f"File {value} already exists. Do you want to overwrite it?")
        if not confirm:
            raise typer.Abort()
        value.unlink()
    return value


@app.command()
def main(
    input_url: str = typer.Argument(
        ...,
        help="url of the Kinescope video",
        parser=parse_url,
    ),
    output_file: Path = typer.Argument(
        None,
        help="path to the output mp4 file",
        callback=callback_output_file,
    ),
    referer: str = typer.Option(
        None,
        "-r",
        "--referer",
        help="Referer url of the site where the video is embedded",
    ),
    best_quality: bool = typer.Option(
        False,
        help="Automatically select the best possible quality",
    ),
    temp: str = typer.Option(
        "./temp",
        help="Path to directory for temporary files",
    ),
) -> None:
    kinescope_video = KinescopeVideo(url=input_url, referer_url=referer)

    downloader = KinescopeDownloader(kinescope_video, temp)

    print("= OPTIONS ============================")
    video_resolutions = downloader.get_resolutions()
    chosen_resolution = (
        video_resolutions[-1]
        if best_quality
        else video_resolutions[
            int(input("   ".join([f"{i + 1}) {r[1]}p" for i, r in enumerate(video_resolutions)]) + "\n> Quality: ")) - 1
        ]
    )
    print(f"[*] {chosen_resolution[1]}p is selected")
    print("======================================")

    print("\n= DOWNLOADING =================")
    downloader.download(
        output_file if output_file else f"{kinescope_video.video_id}.mp4",
        chosen_resolution,
    )
    print("===============================")


if __name__ == "__main__":
    app()
