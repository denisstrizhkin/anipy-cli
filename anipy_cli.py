#!/bin/python
from anipy_cli import cli


# from anipy_cli.misc import keyboard_inter

def main():
    try:
        cli.main()
        pass
    except KeyboardInterrupt:
        # keyboard_iter()
        pass


if __name__ == "__main__":
    main()
