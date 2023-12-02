import unittest
import render

class TestRenderMethods(unittest.TestCase):

    def testBadImages(self):
        res = render.size_check("Render/SizeTest/1000x1200.png")
        self.assertFalse(res, "1000x1020 image should not return True")

        res = render.size_check("Render/SizeTest/1200x1000.png")
        self.assertFalse(res, "1200x1000 image should not return True")

        res = render.size_check("Render/SizeTest/1200x1200.png")
        self.assertFalse(res, "1200x1200 image should not return True")

    def testGoodImage(self):
        res = render.size_check("Render/SizeTest/1000x1000.png")
        self.assertTrue(res, "1000x1000 image should not return False")


if __name__ == "__main__":
     unittest.main(verbosity=2)