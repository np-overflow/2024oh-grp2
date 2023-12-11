# imports
import Render.render as render
import Transform.transform as transform

import os
import sys
import time
import imghdr
import shutil
import argparse
import requests

from uuid import uuid4 as uuid

# modes - add as needed
MODE_BOING = "boioioing"
MODE_DEBUG = "debug"
MODE_TEST = "test"

def banner():
    return """
                                 __   _                    
                                / _| | |                   
   ___   __   __   ___   _ __  | |_  | |   ___   __      __
  / _ \  \ \ / /  / _ \ | '__| |  _| | |  / _ \  \ \ /\ / /
 | (_) |  \ V /  |  __/ | |    | |   | | | (_) |  \ V  V / 
  \___/    \_/    \___| |_|    |_|   |_|  \___/    \_/\_/                                                 

Credits:
    Yu Yang
    Jayden
    Alfred
    Brayden
    """

def parse_args():
    parser = argparse.ArgumentParser(description="boioioing")

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
        help="specifies what effects to apply to the input image, defaults to boioioing",
        default="boioioing",
        choices=[MODE_BOING, MODE_DEBUG, MODE_TEST],
        nargs="?"
    )

    if len(sys.argv) == 1:
        print(banner())
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args

def get_image(url, save_path):
    response = requests.get(url)

    if response.status_code == 200:
        with open(save_path, 'wb') as file_handle: # 'wb' - write mode for binary files
            file_handle.write(response.content)
        
        image_format = imghdr.what(save_path)
        new_path = f"{save_path}.{image_format}"

        os.rename(save_path, new_path)
    else:
        raise Exception("Cannot get image")

    return new_path

def main(): # program main entry point
    save_path = "./temp/"

    if os.path.exists(save_path):
        shutil.rmtree(save_path) # remove temp and its contents

    args = parse_args()
    mode = args.mode
    rng = str(uuid())

    os.mkdir(save_path)

    if args.path is not None:
        image_src = transform.resize_image(args.path)
    else:
        image_src = transform.resize_image(get_image(args.url, save_path+rng))

    if mode == MODE_BOING:
        image_paths = transform.boioioing(image_src)
        while True:
            for i in range(0, len(image_paths), 8): # 8 is step :D
                render.render_image(image_paths[i])
                time.sleep(1 / 727)
                os.system('cls') # clear terminal

if __name__ == "__main__":
    main()