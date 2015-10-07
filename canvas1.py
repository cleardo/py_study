# coding=utf-8
# File: canvas-editing-example-1.py
#
# editing canvas items
# 可编辑画布
#
# fredrik lundh, december 1998
#
# fredrik@pythonware.com
# http://www.pythonware.com
#

from Tkinter import *


class MyCanvas(Frame):
    """
    创建一个frame布局
    """

    def __init__(self, root):

        # 调用frame的初始化
        Frame.__init__(self, root)

        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)

        # standard bindings
        # 双击左键
        self.canvas.bind("<Double-Button-1>", self.set_focus)
        self.canvas.bind("<Button-1>", self.set_cursor)
        self.canvas.bind("<Key>", self.handle_key)

        # 在画布上画两个按钮
        # add a few items to the canvas
        hello_text = self.canvas.create_text(50, 50, text="hello", tag="hello_tag")
        print hello_text
        print self.canvas.itemconfig(hello_text)
        print self.canvas.itemconfigure("hello_tag")
        # print hello_text.itemconfigure()
        self.canvas.create_text(50, 100, text="world")

    def highlight(self, item):
        # mark focused item.
        # note that this code
        # 重新画矩形
        # recreates the
        # rectangle for each update, but that's fast enough for
        # this case.
        # 获取包围当前项的矩形
        bbox = self.canvas.bbox(item)
        print bbox, "hbox"
        self.canvas.delete("highlight")

        if bbox:
            i = self.canvas.create_rectangle(bbox, fill="white", tag="highlight")
            self.canvas.lower(i, item)

    def has_focus(self):
        return self.canvas.focus()

    def has_selection(self):
        # hack to work around bug in Tkinter 1.101 (Python 1.5.1)
        return self.canvas.tk.call(self.canvas._w, 'select', 'item')

    def set_focus(self, event):
        # 判断类型是不是text文本画布
        if self.canvas.type(CURRENT) != "text":
            return

        self.highlight(CURRENT)

        # move focus to item
        # move focus to canvas
        self.canvas.focus_set()
        # set focus to text item
        self.canvas.focus(CURRENT)

        self.canvas.select_from(CURRENT, 0)
        self.canvas.select_to(CURRENT, END)

    def set_cursor(self, event):
        """
        处理单击事件

        :param event:
        :return:
        """
        print "单击"
        print event

        # move insertion cursor
        # 如果有焦点，光标聚焦在文本中
        item = self.has_focus()
        print item

        if not item:
            # 简单的单击，不做任何事
            return # or do something else

        # translate to the canvas coordinate system
        # 将事件坐标转换为canvas坐标
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        print event.x, x

        self.canvas.icursor(item, "@%d,%d" % (x, y))

        self.canvas.select_clear()

    def handle_key(self, event):
        # widget-wide key dispatcher
        item = self.has_focus()

        if not item:
            return

        # 当前焦点的对象
        insert = self.canvas.index(item, INSERT)
        print "insert", insert

        if event.char >= " ":
            # printable character
            if self.has_selection():
                self.canvas.dchars(item, SEL_FIRST, SEL_LAST)
                self.canvas.select_clear()
            self.canvas.insert(item, "insert", event.char)
            self.highlight(item)
        elif event.keysym == "BackSpace":
            if self.has_selection():
                self.canvas.dchars(item, SEL_FIRST, SEL_LAST)
                self.canvas.select_clear()
            else:
                if insert > 0:
                    self.canvas.dchars(item, insert-1, insert)
            self.highlight(item)

        # navigation
        elif event.keysym == "Home":
            self.canvas.icursor(item, 0)
            self.canvas.select_clear()
        elif event.keysym == "End":
            self.canvas.icursor(item, END)
            self.canvas.select_clear()
        elif event.keysym == "Right":
            self.canvas.icursor(item, insert+1)
            self.canvas.select_clear()
        elif event.keysym == "Left":
            self.canvas.icursor(item, insert-1)
            self.canvas.select_clear()
        else:
            print event.keysym
            pass

# 双击文本，允许编辑
# try it out (double-click on a text to enable editing)
root = Tk()

# c = MyCanvas(Tk())
c = MyCanvas(root)
c.pack()

root.mainloop()

