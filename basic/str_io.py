# coding=utf-8

__author__ = 'donglin'


import StringIO

# 使用StringIO作为缓冲区
buf = StringIO.StringIO()

# 使用unicode，可以读取第一个字符
buf.write(u"我hello")

# buf.writelines(["hello", "world测试"])

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    # logger.info(buf.getvalue())

    buf.seek(0)
    logger.info(buf.read(1))
    logger.info(buf.read(2))
