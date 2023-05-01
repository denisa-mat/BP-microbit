from microbit import *
from enum import *


class BUTTON(object):
    """
    button class module

    Params:
        RJ_pin (pin): pin with button

    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pinC = pin1
            self.__pinD = pin8
        elif RJ_pin == J2:
            self.__pinC = pin2
            self.__pinD = pin12
        elif RJ_pin == J3:
            self.__pinC = pin13
            self.__pinD = pin14
        elif RJ_pin == J4:
            self.__pinC = pin15
            self.__pinD = pin16

        self.__pinC.set_pull(self.__pinC.PULL_UP)
        self.__pinD.set_pull(self.__pinD.PULL_UP)

    def C_is_pressed(self) -> bool:
        """
        returns True if button C is pressed

        Return:
            boolean: True/False

        """
        return self.__pinC.read_digital() == 0 and self.__pinD.read_digital() == 1

    def D_is_pressed(self) -> bool:
        """
        returns True if button D is pressed

        Return:
            boolean: 按下返回True, 未按下返回False

        """
        return self.__pinD.read_digital() == 0 and self.__pinC.read_digital() == 1

    def CD_is_pressed(self) -> bool:
        """
        returns True if both buttons C and D are pressed

        Return:
            boolean: True/False

        """
        if self.__pinD.read_digital() == 0 and self.__pinC.read_digital() == 0:
            return True
        else:
            return False
