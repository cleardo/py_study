# coding=utf-8
"""

"""
import Tkinter
from Tkconstants import *

import Pmw

from WidgetRedirector import WidgetRedirector
from Delegator import Delegator


class Percolator:

    def __init__(self, text):
        # XXX would be nice to inherit from Delegator
        self.text = text

        print text

        self.redir = WidgetRedirector(text)

        print "top代理"
        self.top = self.bottom = Delegator(text)

        self.bottom.insert = self.redir.register("insert", self.insert)
        self.bottom.delete = self.redir.register("delete", self.delete)

        self.filters = []

    def close(self):
        while self.top is not self.bottom:
            self.removefilter(self.top)
        self.top = None
        self.bottom.setdelegate(None); self.bottom = None
        self.redir.close(); self.redir = None
        self.text = None

    def insert(self, index, chars, tags=None):
        # Could go away if inheriting from Delegator
        # print "插入操作"
        self.top.insert(index, chars, tags)

    def delete(self, index1, index2=None):
        # Could go away if inheriting from Delegator
        self.top.delete(index1, index2)

    def insertfilter(self, filter):
        # Perhaps rename to pushfilter()?
        # assert isinstance(filter, Delegator)
        # assert filter.delegate is None
        filter.setdelegate(self.top)
        self.top = filter

    def removefilter(self, filter):
        print filter.delegate
        # XXX Perhaps should only support popfilter()?
        assert isinstance(filter, Delegator)
        assert filter.delegate is not None
        f = self.top
        if f is filter:
            self.top = filter.delegate
            filter.setdelegate(None)
        else:
            while f.delegate is not filter:
                assert f is not self.bottom
                f.resetcache()
                f = f.delegate
            f.setdelegate(filter.delegate)
            filter.setdelegate(None)


def _percolator(parent):

    import Tkinter as tk
    import re

    tok_list = [
        'LBRACE',
        'RBRACE',
        'KEY',
        'VALUE'
    ]

    LBRACE = 1
    RBRACE = 2
    KEY = 3
    VALUE = 4

    keyword_list = list()

    color_def = dict()
    color_def['{'] = '#ff0000'
    color_def['}'] = '#ff0000'

    class Lexer(object):
        def __init__(self):
            self.input_buffer = ""
            self.forward = 0
            self.start_pos = ""
            self.end_pos = ""
            self.state = 0
            self.start = 0
            self.lineno = 1
            self.char_pos = 0
            self.lex_begin = 0
            self.buf_len = 0

            # 上一次进行着色的位置
            self.last_hl_pos = 0

        def set_buffer(self, line):
            self.lineno = 1
            self.input_buffer = line
            self.buf_len = len(line)
            self.forward = 0

        def next_char(self):
            print "begin next char"
            print self.buf_len
            print self.forward
            print "end next char"
            if self.buf_len == self.forward:
                return -1
            ch = self.input_buffer[self.forward]
            self.forward += 1
            return ch

        def next_tok(self):
            # print "当前缓冲区", repr(self.input_buffer)
            self.start = 0
            self.state = 0

            while True:
                if self.state == 0:
                    ch = self.next_char()
                    print "forward: ", self.forward
                    print "char read: ", repr(ch)

                    if ch == '"':
                        self.state = 1
                        self.lex_begin = self.forward - 2
                    elif ch == "\n":
                        self.lineno += 1
                    elif ch == -1:
                        return 1

                elif self.state == 1:
                    ch = self.next_char()
                    print "state 1", self.state
                    if ch != '"' and ch != -1:
                        self.state = 1
                    elif ch == '"':
                        print "state 2", self.state
                        self.state = 2
                        self.char_pos = self.forward - 3
                        return KEY
                    elif ch == -1:
                        return 1

        def get_start(self):
            pos = str(self.lineno) + "." + str(self.lex_begin)
            return pos

        def get_end(self):
            pos = str(self.lineno) + "." + str(self.char_pos)
            return pos

    class Parser(object):
        def __init__(self, lex):
            self.lex = lex
            pass

    class Colorize():
        def __init__(self):
            pass

    # 一个新的代理
    class Tracer(Delegator):
        def __init__(self, name, t):
            self.name = name
            self.t = t
            self.lexer = Lexer()
            Delegator.__init__(self, None)

            # 初始化颜色配置
            self.t.tag_configure("op_color", foreground="#ff0000")
            self.t.tag_configure("key_color", foreground="#ff0000")
            self.t.tag_configure("val_color", foreground="#34495e")

        def insert(self, *args):
            print self.name, ": insert", args
            # 支持当前输入字符高亮
            self.delegate.insert(*args)

            # 插入位置
            ins_pos = self.t.index("insert")
            #print "插入位置", ins_pos

            self.lexer.set_buffer(self.t.get("1.0", "end"))

            tok = self.lexer.next_tok()
            st_pos = self.lexer.get_start()
            end_pos = self.lexer.get_end()

            if tok == LBRACE:
                self.t.tag_add("op_color", st_pos, end_pos)
            elif tok == KEY:
                self.t.tag_add("key_color", st_pos, end_pos)
            elif tok == VALUE:
                self.t.tag_add("value_color", st_pos, end_pos)

            tok = self.lexer.next_tok()
            st_pos = self.lexer.get_start()
            print "start pos", st_pos
            end_pos = self.lexer.get_end()

            if tok == LBRACE:
                self.t.tag_add("op_color", st_pos, end_pos)
            elif tok == KEY:
                self.t.tag_add("key_color", st_pos, end_pos)
            elif tok == VALUE:
                self.t.tag_add("value_color", st_pos, end_pos)

            # highlight
            # self.lexer.start_pos

            # 输入文本内容
            #print "文本框内容", repr(self.t.get("1.0", "end"))

            # self.t.tag_add("key_color", "1.0", "1.0+1c")

        def delete(self, *args):
            print self.name, ": delete", args
            self.delegate.delete(*args)

    root = tk.Tk()

    # root.wm_iconbitmap(default='favicon.ico')

    # root.wm_client()
    root.title("QA部Web三组接口测试工具")

    width, height, x, y = list(map(int, re.split('[x+]', parent.geometry())))

    x += 500

    root.geometry("+%d+%d" % (x, y + 150))

    root.option_add('*Entry*foreground', 'white')
    # 背景色设置
    root.option_add('*Entry*background', '#3498db')

    url_val = tk.StringVar()

    def send():
        pass

    def gen_code():
        pass

    url_entry = Pmw.EntryField(root, labelpos='w', label_text='接口url： ', value='http://', validate={})
    url_entry.pack(fill='x', expand=1, padx=0, pady=5)

    urlFrame = tk.Frame(root)

    # url_entry2 = Pmw.EntryField(urlFrame, labelpos='w', label_text='接口url： ', value='http://', validate={})
    # url_entry2.grid(row=2, column=1)

    tk.Label(urlFrame, text='请求类型: ').grid(row=0, sticky=tk.W)
    tk.Entry(urlFrame, width=50, textvariable=url_val).grid(row=0, column=1, columnspan=10)
    tk.Button(urlFrame, text='开始测试', command=send).grid(row=0, column=11, padx=5, pady=2)
    tk.Button(urlFrame, text='生成代码', command=gen_code).grid(row=0, column=12, padx=0, pady=2)
    tk.Button(urlFrame, text='退出', command=quit).grid(row=0, column=13, padx=5, pady=2)

    urlFrame.pack(side=TOP)

    # 结果显示
    text = tk.Text(root)
    p = Percolator(text)

    t1 = Tracer("t1", text)
    p.insertfilter(t1)

    def toggle1():
        print var1.get()
        if var1.get() == 0:
            var1.set(1)
            p.insertfilter(t1)
        elif var1.get() == 1:
            var1.set(0)
            print t1.delegate
            p.removefilter(t1)

    text.pack()

    var1 = tk.IntVar()
    #cb1 = tk.Checkbutton(root, text="支持语法高亮", command=toggle1, variable=var1)
    #cb1.pack()

if __name__ == "__main__":
    r = Tkinter.Tk()
    Pmw.EntryField(r)
    _percolator(r)
    r.withdraw()
    r.mainloop()

