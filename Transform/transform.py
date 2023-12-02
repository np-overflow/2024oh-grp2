import cv2

def resize_image(path):
    img = cv2.imread(path)
    resized_img = cv2.resize(img, (1000, 1000))

    cv2.imwrite(path, resized_img)

    return path