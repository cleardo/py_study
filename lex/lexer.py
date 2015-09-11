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
        pass

    def token(self):
        return Tokmap[0]
