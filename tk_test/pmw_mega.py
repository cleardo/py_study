# coding=utf-8

__author__ = 'linzh'


from Tkinter import *

import Pmw


class Gauge(Pmw.MegaWidget):
    def __init__(self, parent=None, **kw):

        optiondefs = ()

        self.defineoptions(kw, optiondefs)

        Pmw.MegaWidget.__init__(self, parent)

        interior = self.interior()

Pmw.forwardmethods(Gauge, Scale, 'scale')
Pmw.initialise()


if __name__ == "__main__":

    root = Tk()
    root.option_readfile('optionDB')
    root.title('滑动控件')

    gauge = Gauge(root)
    gauge.pack(side=LEFT, padx=1, pady=10)

    root.mainloop()
