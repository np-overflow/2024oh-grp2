# Image to ASCII art generator
With animations! (using opencv)

## Getting started
Ensure `Python` and `pip` are added to PATH.

1. Clone this repository (`git clone https://github.com/np-overflow/2024oh-grp2.git && cd 2024oh-grp2`)
2. Install the dependencies (`pip install -r requirements.txt`)
3. Run `main.py` with desired arguments

## Setting up PyTorch with CUDA for image generation

1. Go to [PyTorch's Get Started page](https://pytorch.org/get-started/locally/).
2. Pick the right version for you and download it with the provided command.

## How to use
Arguments:

1. Local path (`-p OR --path [PATH]`)

    Gets the image locally via file path.

2. URL (`-u OR --url [URL]`)

    Get an image from the internet via URL.

3. Mode (`-m OR --mode [MODE]`)

    Chooses the type of transformation to apply to the passed image. Legal arguments are `boing || static || rotate || spin`. 

    Boing will apply compressions and stretches to the x and y axes, creating a bouncy effect. 

    Static will simply render the image in the terminal.

    Rotate...

    Spin... @jayden

4. AI Generate (`--generate [PROMPT]`)

    Generates an image with the provided prompt.

Example use:
    `python main.py -p C:/Users/user/Desktop/cat.png -m spin`
