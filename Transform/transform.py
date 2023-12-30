import cv2

def resize_image(path):
    img = cv2.imread(path)
    resized_img = cv2.resize(img, (1000, 1000))

    alpha = 2 # kontras
    beta = 0.5 # brigghtness

    adjusted = cv2.convertScaleAbs(resized_img, alpha=alpha, beta=beta)
    cv2.imwrite(path, adjusted)

    return path

def boioioing(path): # expects 1000x1000 input
    img = cv2.imread(path)
    steps = 24

    transform_step = 0.5 / steps

    # store intermediate images
    intermediate = []

    # i wrote this at 3 am dont ask me to change it idk how

    # squeeze y-axis
    for step in range(steps):
        current_height = int(1000 * max(1 - step * transform_step, 0.1))

        squeezed_img = cv2.resize(img, (1000, current_height))

        pad_top = (1000 - current_height) // 2
        pad_bottom = 1000 - current_height - pad_top

        squeezed_img = cv2.copyMakeBorder( # add border to maintain 1000x1000 size
            squeezed_img, 
            pad_top, pad_bottom, 
            0, 0, 
            cv2.BORDER_CONSTANT
            )
        

        intermediate.append(squeezed_img)

    # squeeze x-axis
    for step in range(steps):
        current_width = int(1000 * max(1 - step * transform_step, 0.1))

        squeezed_img = cv2.resize(intermediate[steps-1], (current_width, 1000))

        pad_left = (1000 - current_width) // 2
        pad_right = 1000 - current_width - pad_left

        squeezed_img = cv2.copyMakeBorder( # add border to maintain 1000x1000 size
            squeezed_img, 
            0, 0,
            pad_left, pad_right, 
            cv2.BORDER_CONSTANT
            )
        
        intermediate.append(squeezed_img)

    # unsqueeze y-axis
    for step in range(steps):
        current_height = int(1000 * (1 + step * transform_step * 2))

        stretched_img = cv2.resize(intermediate[steps*2 - 1], (1000, current_height))

        pad_top = (current_height - 1000) // 2
        pad_bottom = current_height - 1000 - pad_top

        stretched_img = stretched_img[pad_top:current_height - pad_bottom, :]

        intermediate.append(stretched_img)


    # unsqueeze x-axis
    for step in range(steps):
        current_width = int(1000 * (1 + step * transform_step * 2))

        stretched_img = cv2.resize(intermediate[steps*3 - 1], (current_width, 1000))

        pad_left = (current_width - 1000) // 2
        pad_right = current_width - 1000 - pad_left

        stretched_img = stretched_img[:, pad_left:current_width - pad_right]

        intermediate.append(stretched_img)


    paths = []
    
    for i, img in enumerate(intermediate):
        path = f"./temp/inter_{i}.png"
        cv2.imwrite(path, img) # saving image for debug purposes

        paths.append(path)

    return paths
    
def rotato(path):
    img = cv2.imread(path)

    # get image dimensions
    height, width = img.shape[:2]
      
    # creates a black border to handle cutoff when rotating images
    # cv2.BORDER_CONSTANT adds a constant colored border i.e full solid colour (black in this case)
    border_size = 400
    border_color = [0, 0, 0] # black
    img = cv2.copyMakeBorder(img, border_size // 2, border_size // 2, border_size // 2, border_size // 2, cv2.BORDER_CONSTANT, value=border_color)
    center = ((width + border_size) // 2, (height + border_size) // 2)
    
    rotated_images = []
    for angle in range(0, 360, 3):
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0) # this creates a transformation matrix for rotation where argument center is the pivot
        
        # warpaffine essentially maps the rotated matrices' coordinates to the original's, read opencv docs for more info
        rotated_img = cv2.warpAffine(img, rotation_matrix, (width + border_size, height + border_size)) 
        rotated_images.append(rotated_img)
 
    paths = []
    for i, rotated_img in enumerate(rotated_images):
        path = f"./temp/rotated_{i}.png"
        cv2.imwrite(path, rotated_img) # saving image for debug purposes
        paths.append(path)

    return paths

def speen(path):
    img = cv2.imread(path)

    # get image dimensions
    height, width = img.shape[:2]
    center = (width // 2, height // 2)
    
    border_size = 500
    border_color = [0, 0, 0]
    
    # this does not create a border but just changes the pivot. it's quite funny
    # this does something funny when border size is 500 btw
    img = cv2.copyMakeBorder(img, border_size // 2, border_size // 2, border_size // 2, border_size // 2, cv2.BORDER_CONSTANT, value=border_color)

    rotated_images = []
    for angle in range(0, 360, 3):
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0) # this creates a transformation matrix for rotation where argument center is the pivot
        
        # warpaffine essentially maps the rotated matrices' coordinates to the original's, read opencv docs for more info
        rotated_img = cv2.warpAffine(img, rotation_matrix, (width + border_size, height + border_size))
        rotated_images.append(rotated_img)
 
    paths = []
    for i, rotated_img in enumerate(rotated_images):
        path = f"./temp/speen_{i}.png"
        cv2.imwrite(path, rotated_img) # saving image for debug purposes
        paths.append(path)

    return paths