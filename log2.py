# coding=utf-8

"""
日志测试程序，该日志会调用不同的日志处理设施
"""

__author__ = 'Administrator'

import logging


class ProgressConsoleHandler(logging.StreamHandler):
    """
    A handler class which allows the cursor to stay on
    one line for selected messages
    """

    # 是否要在同一行写日志，还是换行
    on_same_line = False

    # 重载日志输出函数
    def emit(self, record):
        """
        record: logging.LogRecord
        """
        self.terminator = "\n"

        try:
            # 如果有设置格式化字符串，则会先进行格式化操作
            msg = self.format(record)
            # print "消息", msg
            stream = self.stream
            # print stream

            # 判断是否需要换行
            same_line = hasattr(record, 'same_line')
            # print same_line

            if self.on_same_line and not same_line:
                # 调用换行符
                stream.write(self.terminator)

            stream.write(msg)

            if same_line:
                stream.write('...')
                self.on_same_line = True
            else:
                stream.write(self.terminator)
                # 新起一行，不再同一行了
                self.on_same_line = False

            self.flush()

        except (KeyboardInterrupt, SystemExit):
            raise

        except Exception, errmsg:
            self.handleError(record)


if __name__ == '__main__':
    import time
    progress = ProgressConsoleHandler()
    # console = logging.StreamHandler()

    # 用于设置root logger
    # logging.basicConfig()
    # logger实例
    logger = logging.getLogger('test')
    # 设置级别
    logger.setLevel(logging.DEBUG)
    # 设置handler
    logger.addHandler(progress)

    logger.info('test1')

    for i in range(3):
        # 添加额外属性
        logger.info('remaining %d seconds', i, extra={'same_line': True})
        time.sleep(1)

    logger.info('test2')
