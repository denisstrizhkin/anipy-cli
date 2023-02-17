import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Play Anime from gogoanime in local video-player or Download them."
    )

    parser.add_argument(
        "-q",
        "--quality",
        action="store",
        required=False,
        default="auto",
        help="Change the quality of the video, accepts: best, worst or 360, 480, 720 etc.  Default: best",
    )

    return parser.parse_args()
