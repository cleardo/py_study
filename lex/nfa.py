# coding=utf-8
__author__ = 'linzh'

from input import Lexeme, Input
from lexer import *
input_o = Input()

CCL = 0


class Nfa(object):
    """
    非确定状态机
    """
    def __init__(self):
        """

        :return:
        """
        self.state = 0
        # 边
        self.edge = ''
        # 下一个状态
        self.next1 = ''
        self.next2 = ''
        self.ccl = set()
        # 锚点（行首、行末、首尾、无）
        self.anchor = 0

    def gen(self):
        """
        生成非确定自动机

        基于tompson算法实现

        :return:
        """
        # 起始状态
        sstate = 0

        return sstate


class NfaMachine(object):
    def __init__(self):
        self.states = list()
        self.nstate = 0

    def new_state(self):
        self.states.append(Nfa())
        state = self.states[self.nstate]

        # 状态数增加1
        self.nstate += 1

        return state

    def machine(self):
        p = start = self.new_state()
        p.next1 = ""

        while True:
            # 读到末尾
            p.next2 = Nfa()
            p = p.next2
            p.next1 = self.rule()
            break

        return start

    def rule(self):
        """
        匹配一条词法规则，词法规则由正则表达式、EOS、匹配后执行的动作组合而成

        rule --> expr EOS action
                 ^expr EOS action
                 expr$ EOS action

        action --> <tabs> <动作代码>

        :return:
        """

        nfa_state = Nfa()
        nfa_state.edge = "rule"
        return nfa_state

    def term(self):
        """
        处理单个字符

        term --> [...] | (expr)

        匹配以下单元

        [abc] | [^abc] | . | [] | [\]] | [^] | [\-] | c

        在DFA中，是单个的结点

        :return:
        """
        start = Nfa()

        if False:
            # expr
            pass
        else:
            start.edge = CCL

    def dodash(self):
        """
        匹配 [a-z]这样的字符类

        :return:
        """
        first = ''
        ccl_set = set()
        if not match(EOS) and not match(CCL_END):
            if not match(DASH):
                first = Lexeme
                ccl_set.add(Lexeme)
            else:
                input_o.advance()
                for i in range():
                    ccl_set.add(first)


    def __str__(self):
        pass

if __name__ == "__main__":
    nfa_machine = NfaMachine()
    start = nfa_machine.machine()
    print start
    print start.next2.next1.edge


