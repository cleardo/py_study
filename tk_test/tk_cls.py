# coding=utf-8
__author__ = 'linzh'

import Tkinter as tk


class CoBox(object):
    def __init__(self, master):
        co_frame = tk.Frame(master)
        co_btn = tk.Button(co_frame)
        co_btn.pack()
        co_frame.pack(side=tk.TOP)


root = tk.Tk()
root.geometry("300x200")

co_box = CoBox(root)

root.mainloop()

