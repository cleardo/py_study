# coding=utf-8

__author__ = 'Administrator'

"""
拖动图形

状态机建模
"""

import Tkinter as tk

class SampleApp(tk.Tk):
    '''
    Illustrate how to drag items on a Tkinter canvas

    在画布上进行拖动
    '''
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # create a canvas
        self.canvas = tk.Canvas(width=400, height=400)
        self.canvas.pack(fill="both", expand=True)

        # this data is used to keep track of an
        # item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        # create a couple movable objects
        self._create_token((100, 100), "#3498db")
        self._create_token((200, 100), "#e74c3c")

        # add bindings for clicking, dragging and releasing over
        # any object with the "token" tag
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.OnTokenButtonPress)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.OnTokenButtonRelease)

        self.canvas.tag_bind("token", "<B1-Motion>", self.OnTokenMotion)

    def _create_token(self, coord, color):
        '''Create a token at the given coordinate in the given color
        创建一个状态
        '''

        # 坐标
        (x, y) = coord

        # 设置tag为token
        # 这些tag绑定对应的事件
        self.canvas.create_oval(x-25, y-25, x+25, y+25,
                                outline=color, fill=color, tags="token")

    def OnTokenButtonPress(self, event):
        '''Being drag of an object'''
        # record the item and its location
        # 事件的x坐标和y坐标
        # 查找跟点击事件最近的那个canvas
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def OnTokenButtonRelease(self, event):
        '''
        End drag of an object

        拖动结束
        '''
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def OnTokenMotion(self, event):
        '''
        Handle dragging of an object'''
        # compute how much this object has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]

        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)

        # record the new position
        # 记录新位置
        # 下次拖动时使用
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
