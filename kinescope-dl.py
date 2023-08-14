import click
from kinescope import KinescopeVideo, KinescopeDownloader


@click.command()
@click.option(
    '--referer', '-r',
    required=False, help='Referer url of the site where the video is embedded'
)
@click.option(
    '--best-quality',
    default=False, required=False, help='Automatically select the best possible quality', is_flag=True
)
@click.option(
    '--temp',
    default='./temp', required=False, help='Path to directory for temporary files', type=click.Path()
)
@click.argument('input_url', type=click.STRING)
@click.argument('output_file', type=click.Path())
def main(referer,
         best_quality,
         temp, input_url, output_file):
    """
    kinescope-dl: Video downloader for Kinescope
    https://github.com/anijackich/kinescope-dl

    \b
    <INPUT_URL> is url of the Kinescope video
    <OUTPUT> is path to the output mp4 file
    """

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
          '~                KINESCOPE-DL                ~\n'
          '~         Kinescope videos downloader        ~\n'
          '~ https://github.com/anijackich/kinescope-dl ~\n'
          '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

    is_video_id = 'https' not in input_url

    kinescope_video: KinescopeVideo = KinescopeVideo(
        url=input_url if not is_video_id else None,
        video_id=input_url if is_video_id else None,
        referer_url=referer
    )

    downloader: KinescopeDownloader = KinescopeDownloader(kinescope_video, temp)

    video_resolutions = downloader.get_resolutions()
    chosen_resolution = video_resolutions[-1] if best_quality else video_resolutions[int(input(
        '\n'.join([f'{i + 1}) {r[1]}p' for i, r in enumerate(video_resolutions)]) +
        '\n> QUALITY: '
    )) - 1]

    print('\n= DOWNLOADING =================')
    downloader.download(
        output_file if output_file else f'videos/{kinescope_video.video_id.replace("-", "")}.mp4',
        chosen_resolution
    )
    print('===============================')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('[*] Interrupted')
