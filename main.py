# imports
import sys
import argparse

def banner():
    return """
    Overflow Open House Project!

    Credits:
        Yu Yang
        Jayden
        Alfred
        Brayden
    """

def parse_args():
    parser = argparse.ArgumentParser(description="Overflow Open House Project")

    parser.add_argument(
        "-u",
        "--url",
        help="takes a url argument containing the image"
    )

    parser.add_argument(
        "-p",
        "--path",
        help="specifies a path for the program to get image from"
    )

    parser.add_argument(
        "-m",
        "--mode",
        help="specifies what effects to apply to the input image, or defaults to boioioing"
    )

    if len(sys.argv) == 1:
        print(banner())
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args

def main(): # program main entry point
    args = parse_args()


if __name__ == "__main__":
    main()