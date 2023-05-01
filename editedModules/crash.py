from microbit import *
from enum import *


class CRASH(object):
    """
    crash class module

    Params:
        RJ_pin (pin): pin with sensor

    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pin = pin8
        elif RJ_pin == J2:
            self.__pin = pin12
        elif RJ_pin == J3:
            self.__pin = pin14
        elif RJ_pin == J4:
            self.__pin = pin16

        self.__pin.set_pull(self.__pin.PULL_UP)

    def crash_is_pressed(self) -> bool:
        """
        returns True if crash is pressed, False otherwise
        
        Params: NONE

        Return:
            boolean: True/False

        """
        return self.__pin.read_digital() == 0
