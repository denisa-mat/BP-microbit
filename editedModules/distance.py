from microbit import *
from time import sleep_us
from machine import time_pulse_us
from enum import *


class DISTANCE(object):
    """
    HC_SR04 Distance module class

    Params:
        pin_trig (pin): Trig
        pin_echo (pin): Echo

    Returns:
        distance: (object)
    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pin_e = pin8
            self.__pin_t = pin1
        elif RJ_pin == J2:
            self.__pin_e = pin12
            self.__pin_t = pin2
        elif RJ_pin == J3:
            self.__pin_e = pin14
            self.__pin_t = pin13
        elif RJ_pin == J4:
            self.__pin_e = pin16
            self.__pin_t = pin15

    def get_distance(self, unit=0) -> float:
        """
        returns distance

        Params:
            Optional[unit] (int): 0 for metric (default), 1 for inches

        Returns:
            distance (float): measured distance, unit depends on optional param, metric is default
        """
        if unit != 1 or unit != 0:
            raise ValueError('unit has to be 0 or 1')

        self.__pin_e.read_digital()
        self.__pin_t.write_digital(1)
        sleep_us(10)
        self.__pin_t.write_digital(0)
        ts = time_pulse_us(self.__pin_e, 1, 25000)

        distance = ts * 9 / 6 / 58
        if unit == 0:
            return distance
        elif unit == 1:
            return distance / 254
        return 0
