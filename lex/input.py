# coding=utf-8
__author__ = 'linzh'

import string
import StringIO

Lexeme = ''


class Input(object):
    def __init__(self, filename="rege.l"):
        self.file = filename
        self.fp = open(self.file, 'r')
        self.input_buf = StringIO.StringIO()

    def get_line(self):
        line = self.fp.readline()
        self.input_buf.write(line)
        print self.input_buf.getvalue()

    def get_expr(self):
        """
        获取一条正则表达式以及关联的action

        :return:
        """

        lookahead = self.get_line()

    def advance(self):
        """
        下一个字符

        :return:
        """

        # 是否进入字符串解析
        inquote = 0

        # 看到一个转义字符
        saw_esc = 0

        pass


if __name__ == "__main__":
    inp_o = Input()
    inp_o.get_line()
    print inp_o.advance()
