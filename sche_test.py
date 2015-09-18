# coding=utf-8

__author__ = 'linzh'

import time
import sched

schedule = sched.scheduler(time.time, time.sleep)

global tt

tt = time.time()


def perform_command(cmd, inc):
    print(time.time())
    print("tt", time.time() - tt)


def timming_exe(cmd, inc=60):
    """
    默认 60秒后执行cmd

    :param cmd:
    :param inc:
    :return:
    """
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    schedule.run()


if __name__ == "__main__":
    tt = time.time()
    timming_exe("echo %time%", 5)
