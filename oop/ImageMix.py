# ImageMix.py
# 图片混合(+-*/)
import numpy as np
from PIL import Image

class ImageObject:
    def __init__(self, path = ""):
        self.path = path
        try:
            self.data = np.array(Image.open(path))
        except:
            self.data = None
    def __add__(self, other):
        image = ImageObject()
        # 直接使用np.array对象的加法，利用np.mod()函数对元素取模
        # RGB颜色范围是0-255，任何异常则将第一个加数的图像作为输出
        try:
            image.data = np.mod(self.data + other.data, 255)
        except:
            image.data = self.data
        return image
    def __sub__(self, other):
        image = ImageObject()
        try:
            image.data = np.mod(self.data - other.data, 255)
        except:
            image.data = self.data
        return image
    def __mul__(self, factor):
        image = ImageObject()
        try:
            image.data = np.mod(self.data * factor, 255)
        except:
            image.data = self.data
        return image
    def __truediv__(self, factor):
        image = ImageObject()
        try:
            image.data = np.mod(self.data // factor, 255)
        except:
            image.data = self.data
        return image
    def saveImage(self, path):
        try:
            im = Image.fromarray(self.data)
            im.save(path)
            return True
        except:
            return False

a = ImageObject("source/earth.jpg")
b = ImageObject("source/gray.jpg")
(a + b).saveImage("source/result_add.png")
(a - b).saveImage("source/result_sub.png")
(a * 2).saveImage("source/result_mul.png")
(a / 2).saveImage("source/result_div.png")