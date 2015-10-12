# coding=utf-8

__author__ = 'linzh'

from Tkinter import *

root = Tk()

def enter(event):
    print "进入Frame: x=%d, y=%d" % (event.x, event.y)

frame = Frame(root, width=150, height=150)

frame.bind('<Any-Enter>', enter)

frame.pack()

root.mainloop()
