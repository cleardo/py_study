# coding=utf-8
from timeit import Timer

__author__ = 'donglin'


from io import StringIO

# from cStringIO import StringIO

def meth1(str1):
    a = []

    for i in range(100):
        a.append(str1)

    return ''.join(a)


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    str1 = meth1("hello\n")
    # logger.info(str1)

    print(Timer("meth1(\"hello\")", "from __main__ import meth1").timeit(number=1))



