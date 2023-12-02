import unittest
import render

class TestRenderMethods(unittest.TestCase):

    def testBadImages(self):
        res = render.size_check("Render/SizeTest/1000x1020.png")
        self.assertFalse(res, "500x520 image should not return True")

        res = render.size_check("Render/SizeTest/1200x1000.png")
        self.assertFalse(res, "520x500 image should not return True")

        res = render.size_check("Render/SizeTest/1200x1200.png")
        self.assertFalse(res, "520x520 image should not return True")

    def testGoodImage(self):
        res = render.size_check("Render/SizeTest/1000x1000.png")
        self.assertTrue(res, "500x500 image should not return False")


if __name__ == "__main__":
     unittest.main(verbosity=2)