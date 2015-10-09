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
# *
CLOSURE = 9
DASH = 10
END_OF_INPUT = 11
L = 12
OPEN_CURLY = 13
OPEN_PAREN = 14
OPTIONAL = 15
OR = 16
PLUS_CLOSE = 17
UNUSED = 18

Tokmap = [
    # 0
    # ^@ ^A ^B ^C ^D ^E ^F ^G ^H ^I ^J ^K ^L ^M ^N
    L, L, L, L, L, L, L, L, L, L, L, L, L, L, L,
    #  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  */
    #  ^O  ^P  ^Q  ^R  ^S  ^T  ^U  ^V  ^W  ^X  ^Y  ^Z  ^[  ^\  ^]  */
    L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,
    #  30  31  32      33  34  35  36      37  38  39              */
    #  ^^  ^_  SPACE   !   "   #   $       %   &   '               */
    L,  L,  L,      L,  L,  L,  AT_EOL, L,  L,  L,
    #  40          41              42       43          44 45    46*/
    #  (           )               *        +           ,  -     . */
    OPEN_PAREN, CLOSE_PAREN,    CLOSURE, PLUS_CLOSE, L, DASH, ANY,
    #  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  */
    #  /   0   1   2   3   4   5   6   7   8   9   :   ;   <   =   */
    L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,
    #  62  63                                                      */
    #  >   ?                                                       */
    L,  OPTIONAL,
    #  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  */
    #  @   A   B   C   D   E   F   G   H   I   J   K   L   M   N   */
    L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,
    #  79  80  81  82  83  84  85  86  87  88  89  90              */
    #  O   P   Q   R   S   T   U   V   W   X   Y   Z               */
    L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,
    #  91          92  93          94                              */
    #  [           \   ]           ^                               */
    CCL_START,  L,  CCL_END,    AT_BOL,
    #  95  96  97  98  99  100 101 102 103 104 105 106 107 108 109 */
    #  _   `   a   b   c   d   e   f   g   h   i   j   k   l   m   */
    L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,
    # 110 111 112 113 114 115 116 117 118 119 120 121 122 */
    # n   o   p   q   r   s   t   u   v   w   x   y   z           */
    L,    L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,  L,
    # 123         124     125             126                         */
    # {           |       }           DEL                         */
    OPEN_CURLY,   OR, CLOSE_CURLY,    L
]

def match():
    pass


class Lexer(object):
    def __init__(self):
        """

        :return:
        """

        # 词素文本
        self.lexeme = ""

        # 词素
        self.tok = None

        # 读写对象，实现IO接口
        self.io = None
        self.buf = ""
        self.ptr = 0

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
        if self.ptr > len(self.buf):
            # 指针
            return True
        else:
            return False

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

        tok_idx = ord(ch)

        # 如果是宏，则获取对应的宏，将当前输入压入堆栈，设置当前字符缓冲区为宏文本
        return Tokmap[tok_idx]

    def match(self, tok):
        """
        判断是否匹配token

        :param tok:
        :return:
        """
        if self.tok == tok:
            return True

    def token(self):
        return Tokmap[0]

    def tok_len(self):
        return len(Tokmap)


if __name__ == "__main__":
    print "lex输入文件词法解析，在模板驱动程序中使用"

    def get_line():
        fp = open("demo.l", "r")
        return fp

    lexer = Lexer()
    lexer.set_io(get_line)
    # lexer.advance()
    print lexer.advance()

    print "token length"
    print lexer.tok_len()
    print chr(122)
    print repr(chr(0))
