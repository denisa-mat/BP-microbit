from microbit import *

NEZHA_ADDR = 0x10

class MOTOR(object):
    """
    servo module class

    Params:
        servo_pin: 1, 2, 3, 4

    """
    def __init__(self, servo_pin):
        if servo_pin not in [1, 2, 3, 4]:
            raise ValueError("servo_pin must be in [1, 2, 3, 4]")
        i2c.init()
        self.__servo_pin__ = servo_pin

    def set_servo(self, angle):
        """        
        Sets angle to servo on given pin
        Params:
            servo (int): valid values within 1,2,3,4
            angle (int): valid values within (0,180)
        Return:
            NONE
        """
        if angle > 180 or angle < 0:
            raise ValueError('angle error,0~180')
        if self.__servo_pin__ == 1:
            i2c.write(NEZHA_ADDR, bytearray([0x10, angle, 0, 0]))
        elif self.__servo_pin__ == 2:
            i2c.write(NEZHA_ADDR, bytearray([0x11, angle, 0, 0]))
        elif self.__servo_pin__ == 3:
            i2c.write(NEZHA_ADDR, bytearray([0x12, angle, 0, 0]))
        elif self.__servo_pin__ == 4:
            i2c.write(NEZHA_ADDR, bytearray([0x13, angle, 0, 0]))