from microbit import *
from enum import *


class LED(object):
    """
    led class module
    Params:
        RJ_pin (pin): pin with sensor

    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pin = pin1
        elif RJ_pin == J2:
            self.__pin = pin2
        elif RJ_pin == J3:
            self.__pin = pin13
        elif RJ_pin == J4:
            self.__pin = pin15
        self.__is_on = False
        self.__brightness = 0

    def set_led(self, state: bool, brightness=100) -> None:
        """
        sets led on if state is True, otherwise off, and brightness with default value 100

        Params:
            state (boolean): True/False
            brightness (int): <0,100>

        Return: NONE
        """
        if brightness < 0 or brightness > 100:
            raise ValueError("brightness error, must 0 <= brightness <= 100")
        
        if not state:
            self.__pin.write_analog(0)
        elif state:
            brightness = (brightness * 1023) // 100;
            self.__pin.write_analog(brightness)
            
        self.__is_on = state
        if self.__is_on:
            self.__brightness = brightness
        else:
            self.__brightness = 0

    def set_led_on(self) -> None:
        """
        sets led on with default brightness 80

        Params: NONE

        Return: NONE
        """
        self.set_led(True, brightness=80)


    def set_led_off(self) -> None:
        """
        sets led off

        Params: NONE

        Return: NONE
        """
        if self.__is_on:
            self.set_led(False)

    def set_led_brightness(self, brightness) -> None:
        """
        sets brightness

        Params:
            brightness (int): <0,100>

        Return: NONE
        """
        if self.__is_on:
            self.set_led(True, brightness=brightness)

    def get_is_on(self) -> bool:
        """
        returns state, False if led is off, True otherwise

        Params: NONE

        Return: True/False
        """
        return self.__is_on

    def get_brightness(self) -> int:
        """
        returns brightness

        Params: NONE

        Return:
            (int) brightness
        """
        return self.__brightness
