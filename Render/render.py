import cv2
from ascii_magic import AsciiArt

def render_image(path):
    frame = AsciiArt.from_image(path)

    frame.to_terminal(monochrome=True)

def size_check(path):
    img = cv2.imread(path)
    w, h, _ = img.shape

    return w == h == 1000