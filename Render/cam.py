import cv2
from uuid import uuid4 as uuid

def get_cam_input(save_path):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        name = str(uuid())  
        cv2.imwrite(f"{save_path}{name}.png", frame)
        yield f"./temp/{name}.png"