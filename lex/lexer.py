# coding=utf-8
__author__ = 'linzh'

EOS = 1
ANY = 2
AT_BOL = 3
AT_EOL = 4
CCL_END = 5
CCL_START = 6
CLOSE_CURLY = 7
CLOSE_PAREN = 8
CLOSEURE = 9
DASH = 10
END_OF_INPUT = 11
L = 12
OPEN_CURLY = 13
OPEN_PAREN = 14
OPTIONAL = 15
OR = 16
PLUS_CLOSE = 17

Tokmap = [
    L, L
    # n o p q r s t u v w x y z

]

def match():
    pass


class Lexer(object):
    def __init__(self):
        """

        :return:
        """

        # 读写对象，实现IO接口
        self.io = None
        self.buf = ""

    def set_io(self, fp):
        """
        设置IO函数

        #. 从文件读写
        #. 从终端读写

        :return:
        """
        self.io = fp()

        return fp

    def end_of_buf(self):
        """
        判断是否到达了缓冲区的末尾

        :return:
        """
        pass

    def advance(self):
        """
        从字符缓冲区读入一个字符

        :return:
        """

        if self.end_of_buf():
            # 如果到达缓冲区末尾，则需要从文件中读取下一行数据
            data = self.io.readline()
            self.buf = data

        ch = self.io.read(1)
        return ch

    def token(self):
        return Tokmap[0]


if __name__ == "__main__":
    print "lex输入文件词法解析，在模板驱动程序中使用"

    def get_line():
        fp = open("demo.l", "r")
        return fp

    lexer = Lexer()
    lexer.set_io(get_line)
    # lexer.advance()
    print lexer.advance()

