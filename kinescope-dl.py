import click
from kinescope import KinescopeVideo, KinescopeDownloader


@click.command()
@click.option(
    '--referer', '-r',
    default='', required=False, help='Referer url of the site where the video is embedded'
)
@click.option(
    '--best-quality',
    default=False, required=False, help='Automatically select the best possible quality', is_flag=True
)
@click.option(
    '--ffmpeg-bin',
    default=None, required=False, help='Path to FFmpeg binary', type=click.Path()
)
@click.option(
    '--mp4decrypt-bin',
    default=None, required=False, help='Path to mp4decrypt binary', type=click.Path()
)
@click.option(
    '--temp',
    default='./temp', required=False, help='Path to directory for temporary files', type=click.Path()
)
@click.argument('source', type=click.STRING)
@click.argument('output', default=None, required=False, type=click.Path())
def main(referer,
         best_quality,
         ffmpeg_bin, mp4decrypt_bin,
         temp, source, output):
    """
    kinescope-dl: Video downloader for Kinescope
    https://github.com/anijackich/kinescope-dl

    \b
    <SOURCE> is url or id of video
    <OUTPUT> is output mp4 file (optional)
    """

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          '~                KINESCOPE-DL                ~\n'
          '~         Kinescope videos downloader        ~\n'
          '~ https://github.com/anijackich/kinescope-dl ~\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    is_video_id = 'https' not in source

    kinescope_video: KinescopeVideo = KinescopeVideo(
        url=source if not is_video_id else None,
        video_id=source if is_video_id else None,
        referer_url=referer
    )

    downloader: KinescopeDownloader = KinescopeDownloader(kinescope_video, temp, ffmpeg_bin, mp4decrypt_bin)

    video_resolutions = downloader.get_resolutions()
    chosen_resolution = video_resolutions[-1] if best_quality else video_resolutions[int(input(
        '\n'.join([f'{i + 1}) {r[1]}p' for i, r in enumerate(video_resolutions)]) +
        '\n> QUALITY: '
    )) - 1]

    print('\n= DOWNLOADING =================')
    downloader.download(
        output if output else f'videos/{kinescope_video.video_id.replace("-", "")}.mp4',
        chosen_resolution
    )
    print('===============================')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('[*] Interrupted')
