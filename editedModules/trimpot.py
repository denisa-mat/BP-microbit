from microbit import *
from enum import *


class TRIMPOT(object):
    """
    trimpot class module

    Params:
        RJ_pin (pin): pin with trimpot
    """
    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pin = pin1
        elif RJ_pin == J2:
            self.__pin = pin2
        else:
            raise ValueError("pin error, must be J1 or J2")

    def get_trimpot_value(self):
        """
        returns value on trimpot

        Return:
            analog: value
        """
        return self.__pin.read_analog()
