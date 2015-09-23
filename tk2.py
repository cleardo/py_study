# coding=utf-8
import Tkinter as tk

import tkFont

from Tkconstants import END


# 继承tk.Tk
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Toolbar
        self.toolbar = tk.Frame()

        # 加粗按钮
        self.bold = tk.Button(name="toolbar", text="bold加粗",
                              borderwidth=1, command=self.OnBold,)

        self.bold.pack(in_=self.toolbar, side="left")

        ## Main part of the GUI
        # I'll use a frame to contain the widget and 
        # scrollbar;
        # 使用frame
        # it looks a little nicer that way...
        text_frame = tk.Frame(borderwidth=1, relief="sunken")

        self.text = tk.Text(wrap="word", background="white", 
                            borderwidth=0, highlightthickness=0)

        self.vsb = tk.Scrollbar(orient="vertical", borderwidth=1,
                                command=self.text.yview)

        # 设置滚动命令
        self.text.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(in_=text_frame, side="right", fill="y", expand=False)

        self.text.pack(in_=text_frame, side="left", fill="both", expand=True)

        self.toolbar.pack(side="top", fill="x")

        text_frame.pack(side="bottom", fill="both", expand=True)

        # clone the text widget font and use it as a basis for some
        # tags
        # 复制 text widget
        print self.text.cget("font")

        # 配置字体属性
        # 不同的关键字具有不同的属性
        bold_font = tkFont.Font(self.text, self.text.cget("font"))
        bold_font.configure(weight="bold")

        self.text.tag_configure("bold", font=bold_font)

        self.text.tag_configure("misspelled", foreground="red", underline=True)

        # set up a binding to do simple spell check.
        # 进行一些简单的检查
        # This merely
        # checks the previous word when you type a space. For production
        # use you'll need to be a bit more intelligent about when
        # to do it.
        self.text.bind("<space>", self.Spellcheck)

        # initialize the spell checking dictionary. YMMV.
        self._words = open("dict_checker").read().split("\n")

        print self._words

        self.text.insert(END, "text insert use import")

    def Spellcheck(self, event):
        '''
        Spellcheck the word preceeding the insertion point
        插入点的索引
        "insert" "end"
        '''
        index = self.text.search(r'\s', "insert", backwards=True, regexp=True)
        print index
        print "%s+1c" % index

        if index == "":
            index ="1.0"
        else:
            index = self.text.index("%s+1c" % index)

        print index
        # 获取到插入点的字符
        word = self.text.get(index, "insert")
        print "word", word

        if word in self._words:
            self.text.tag_remove("misspelled", index, "%s+%dc" % (index, len(word)))
        else:
            self.text.tag_add("misspelled", index, "%s+%dc" % (index, len(word)))

    def OnBold(self):
        '''Toggle the bold state of the selected text'''

        # toggle the bold state
        # based on the first character
        # in the selected range.
        # If bold, unbold it. If not
        # bold, bold it.
        # 基于第一个字符决定状态
        # 选区操作
        current_tags = self.text.tag_names("sel.first")
        print "第一个字符的tag， tuples"
        print current_tags

        if "bold" in current_tags:
            # first char is bold, so unbold the range
            # 将选区的字符进行处理
            self.text.tag_remove("bold", "sel.first", "sel.last")
        else:
            # first char is normal, so bold the whole selection
            self.text.tag_add("bold", "sel.first", "sel.last")


if __name__ == "__main__":
    app = App()
    app.update()
    app.mainloop()