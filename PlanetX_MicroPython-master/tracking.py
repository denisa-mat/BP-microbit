from microbit import *
from enum import *


class TRACKING(object):
    """基本描述

    两路巡线模块

    Args:
        RJ_pin (pin): 连接端口

    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pinL = pin1
            self.__pinR = pin8
        elif RJ_pin == J2:
            self.__pinL = pin2
            self.__pinR = pin12
        elif RJ_pin == J3:
            self.__pinL = pin13
            self.__pinR = pin14
        elif RJ_pin == J4:
            self.__pinL = pin15
            self.__pinR = pin16

        self.__pinL.set_pull(self.__pinL.PULL_UP)
        self.__pinR.set_pull(self.__pinR.PULL_UP)

    def get_state(self):
        """基本描述

        返回当前巡线头状态

        Returns:
            00 均在白色
            10 左黑右白
            01 左白右黑
            11 均在黑色

        """
        if self.__pinL.read_digital() == 1 and self.__pinR.read_digital() == 1:
            return 00
        elif self.__pinL.read_digital() == 0 and self.__pinR.read_digital() == 1:
            return 10
        elif self.__pinL.read_digital() == 1 and self.__pinR.read_digital() == 0:
            return 01
        elif self.__pinL.read_digital() == 0 and self.__pinR.read_digital() == 0:
            return 11
        else:
            print("Unknown ERROR")


if __name__ == '__main__':
    trc = TRACKING(J1)
    while True:
        if trc.get_state() == 10:
            display.show(Image.HAPPY)
        elif trc.get_state() == 00:
            display.show(Image.SAD)

