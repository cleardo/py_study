# coding=utf-8
__author__ = 'Administrator'

import os
os.environ['TKDND_LIBRARY'] = ""

import Tkinter

from untested_tkdnd_wrapper import TkDND

root = Tkinter.Tk()

dnd = TkDND(root)

entry = Tkinter.Entry()
entry.pack()


def handle(event):
    event.widget.insert(0, event.data)

# 可以将文件拖到该处
dnd.bindtarget(entry, handle, 'text/uri-list')

root.mainloop()
