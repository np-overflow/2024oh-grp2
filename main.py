import requests
from Render import render

# program entry point

def __main__():
    URL_TO_IMAGE = input("Enter URL to image: ")
    image = requests.get(URL_TO_IMAGE).content

    # TO IMPLEMENT : resize image