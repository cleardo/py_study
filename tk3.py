# coding=utf-8
import Tkinter as tk
from Tkconstants import END


class CustomText(tk.Text):
    '''A text widget with a new method, HighlightPattern 

    example:

    text = CustomText()
    text.tag_configure("red",foreground="#ff0000")
    text.HighlightPattern("this should be red", "red")

    The highlight_pattern method is a simplified python 
    version of the tcl code at http://wiki.tcl.tk/3246
    '''
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end", regexp=False):
        '''
        Apply the given tag to all text that matches the given pattern
        If 'regexp' is set to True, pattern will be treated as a regular expression
        如果regexp 设置为true，则pattern为正则匹配
        '''
        start = self.index(start)
        print start
        # 获取最后一行的索引
        end = self.index(end)
        print end

        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        print "count", count
        print "pattern: ", pattern
        print "regex: ", regexp

        while True:
            index = self.search(pattern, "matchEnd", "searchLimit", count=count, regexp=regexp)
            # 搜索结果

            if index == "":
                break

            # 设置标记
            self.mark_set("matchStart", index)
            print "matchStart: ", index

            # 1.0 + 2c 表示索引+长度
            print "matchEnd: %s+%sc" % (index, count.get())
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))

            # 添加tag
            self.tag_add(tag, "matchStart", "matchEnd")
            
            
text = CustomText()

# 定义标签
text.tag_configure("red", foreground="#ff0000")

# 初始化编辑器文本
text.insert(END, "this should be end red\ntest\nend")

# 应用red标签在匹配的文本上
text.highlight_pattern("is", "red")

text.pack()

text.mainloop()