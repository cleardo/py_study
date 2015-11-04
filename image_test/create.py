# coding=utf-8
__author__ = 'linzh'

import Image

# 新建一个image对象
newIm1 = Image.new("RGBA", (640, 480), (255, 0, 0))
newIm1.show()

# 创建
newIm2 = Image.new("P", (640, 480), 0)
newIm2.show()

