# coding=utf-8

__author__ = 'donglin'

from Tkinter import *

root = Tk()

root.geometry("300x200+100+100")

btn = Button(root)

btn.place(relx=0.5)

btn2 = Button(root, text="btn2")

btn2.pack(side=TOP, pady=50)

root.mainloop()

