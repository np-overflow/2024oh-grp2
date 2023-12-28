# imports
import Render.render as render
import Render.imagen as imagen
import Transform.transform as transform

import os
import sys
import time
import imghdr
import shutil
import argparse
import requests

from uuid import uuid4 as uuid


def banner():
    return """
    credit: yy
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
        choices=["boioioing", "static", "rotato", "speen"],
        nargs="?"
    )

    parser.add_argument(
        "--generate",
        help="generate an image with stable diffusion",
        default="NO_GEN",
        nargs="?"
    )

    parser.add_argument(
        "--gif",
        help="keep urself safe"
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
    if args.generate != "NO_GEN":
    #     # with openai api
        #args.url = imagen.generate(args.generate) 

        args.path = imagen._generate(args.generate, save_path+rng)

    if args.path is not None:
        image_src = transform.resize_image(args.path)
    else:
        image_src = transform.resize_image(get_image(args.url, save_path+rng))

    match mode:
        case "boioioing":
            image_paths = transform.boioioing(image_src)

            while True:
                for i in range(0, len(image_paths), 8): # 8 is step :D
                    render.render_image(image_paths[i])
                    time.sleep(1 / 727)
                    os.system('cls') # clear terminal

        case "static":
            render.render_image(image_src)
            
        case "rotato":
            image_paths = transform.rotato(image_src)
            while True:
                for i in range(0, len(image_paths), 9): # 9 is step :P
                    render.render_image(image_paths[i])
                    time.sleep(1/20) 
                    os.system('cls')  # clear terminal

        case "speen":
            image_paths = transform.speen(image_src)
            while True:
                for i in range(0, len(image_paths), 9): # 9 is step XD
                    render.render_image(image_paths[i])
                    time.sleep(1/20) 
                    os.system('cls')  # clear terminal
                    
        case default:
            print("not implemented")

# import imageio
# if args.gif == "a":
#     img = []
#     for i in range(0, len(image_paths)):

#         img.append(imageio.imread(image_paths[i]))

#     imageio.mimsave('wallahi.gif', img)

if __name__ == "__main__":
    main()