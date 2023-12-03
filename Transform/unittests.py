import cv2
import numpy
import random
import unittest
import transform

class TestTransformMethods(unittest.TestCase):

    def testProperResize(self):
        path = "./temp/validation_image.png"
        expected = (1000, 1000)
        
        # generate a 2d array with random dimensions and write to image
        blank_img = numpy.zeros((random.randint(1,2000), random.randint(1,2000)), dtype=numpy.uint8)
        cv2.imwrite(path, blank_img) 

        transform.resize_image(path)
        w, h, _ = cv2.imread(path).shape
        self.assertEqual((w, h), expected)


if __name__ == "__main__":
     unittest.main(verbosity=2)