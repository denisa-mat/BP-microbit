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

    def set_led(self, state, brightness=100):
        """
        sets led on if state is True, otherwise off, and brightness with default value 100

        Params:
            state (boolean): True/False
            brightness (int): <0,100>

        Return: NONE
        """
        if not state:
            self.__pin.write_analog(0)
        elif state:
            brightness = (brightness * 1023) // 100;
            self.__pin.write_analog(brightness)
        else:
            raise ValueError("brightness error, must 0 <= brightness <= 100")
        self.__is_on = state
        self.__brightness = brightness

    def set_led_on(self):
        """
        sets led on with default brightness 80

        Params: NONE

        Return: NONE
        """
        self.set_led(True, brightness=80)


    def set_led_off(self):
        """
        sets led off

        Params: NONE

        Return: NONE
        """
        if self.__is_on:
            self.set_led(False)

    def set_led_brightness(self, brightness):
        """
        sets brightness

        Params:
            brightness (int): <0,100>

        Return: NONE
        """
        if self.__is_on:
            self.set_led(True, brightness=brightness)

    def get_is_on(self):
        """
        returns state, False if led is off, True otherwise

        Params: NONE

        Return: True/False
        """
        return self.__is_on

    def get_brightness(self):
        """
        returns brightness

        Params: NONE

        Return:
            (int) brightness
        """
        return self.__brightness
