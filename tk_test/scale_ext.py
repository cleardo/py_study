# coding=utf-8

__author__ = 'linzh'


from Tkinter import *

import Pmw


class MyScale(Pmw.MegaWidget):
    def __init__(self, parent=None, **kw):
        optiondefs = (
            ('min', 0, Pmw.INITOPT),
        )

        self.defineoptions(kw, optiondefs)

        print self['min']

        Pmw.MegaWidget.__init__(self, parent)

        interior = self.interior()

        self.text_var = StringVar()

        self.myscale = self.createcomponent("myscale", (), None, Frame, (interior, ), borderwidth=1)
        self.btn = Label(self.myscale, text="0", textvariable=self.text_var)
        self.btn.pack(side=LEFT, padx=20)
        self.myscale.grid()

        # 构造组件，基于已有的控件Scale
        self.scale = self.createcomponent("scale", (), None, Scale, (interior, ), command=self.up_btn)
        self.scale.grid()

        # self.initialiseoptions(MyScale)

    def up_btn(self, value):
        print "更新值", value
        self.text_var.set(value)

root = Tk()
root.title("组合控件测试")
root.geometry("500x500+200+100")
# Pmw.initialise()

my_scale = MyScale(root, min=2, arg="1")
my_scale.pack(side=TOP)

root.mainloop()
