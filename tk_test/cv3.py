# coding=utf-8

__author__ = 'linzh'

import Tkinter as tk
from tkFileDialog import askopenfilename
import Image
import cof.image.gauss as CoImage

import cv2

import numpy as np


def thresh_callback(thresh, blur, img):
    edges = cv2.Canny(blur, thresh, thresh*2)

    drawing = np.zeros(img.shape, np.uint8)     # Image to draw the contours

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:

        # color = np.random.randint(0,255,(3)).tolist()  # Select a random color
        color = [255, 255, 255]

        cv2.drawContours(drawing,[cnt],0,color,2)

    cv2.imwrite('output.png', drawing)


def open_img():
    ofile = askopenfilename()
    ofile = ofile.encode("utf-8")

    output = CoImage.gauss(ofile)
    print output
    myim = Image.open(output)
    myim.thumbnail((500, 500))
    myim.show()


root = tk.Tk()

img_btn = tk.Button(root, text="打开图像", command=open_img)

img_btn.pack(side=tk.TOP, expand=tk.YES)

root.geometry("300x200+100+100")

root.mainloop()
