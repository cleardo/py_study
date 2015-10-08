# coding=utf-8

__author__ = 'linzh'

import cof.image.gauss as CoGauss

import Tkinter as tk

from tkFileDialog import askopenfilename

def open_file():
    ofile = askopenfilename()
    ofile = ofile.encode("utf-8")

    output = CoGauss.gauss(ofile)
    print output


root = tk.Tk()
root.geometry("300x200+200+100")

btn = tk.Button(root, text="打开图像", command=open_file)
btn.pack(side=tk.LEFT)

root.mainloop()
