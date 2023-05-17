from microbit import *

J1 = pin8
J2 = pin12
J3 = pin14
J4 = pin16

NEZHA_ADDR = 0x10

class NEZHA(object):
    """
    nezha module class

    """
    def __init__(self):
        i2c.init()

    def set_motor(self, motor, speed):
        """
        sets speed to motor on given pin
        Params:
            motor (int): valid values within 1,2,3,4
            speed (int): valid values within -100~100

        Return:
            NONE
        """
        if speed > 100 or speed < -100:
            raise ValueError('speed error,-100~100')
        if motor > 4 or motor < 1:
            raise ValueError('select motor error,1,2,3,4')
        if speed < 0:
            i2c.write(NEZHA_ADDR, bytearray([motor, 0x02, speed * -1, 0]))
        else:
            i2c.write(NEZHA_ADDR, bytearray([motor, 0x01, speed, 0]))
    
    def set_servo(self, servo, angle):
        """        
        Sets angle to servo on given pin
        Params:
            servo (int): valid values within 1,2,3,4
            angle (int): valid values within (0,180)
        Return:
            NONE
        """
        if servo > 4 or servo < 1:
            raise ValueError('select servo error,1,2,3,4')
        if angle > 180 or angle < 0:
            raise ValueError('angle error,0~180')
        if servo == 1:
            i2c.write(NEZHA_ADDR, bytearray([0x10, angle, 0, 0]))
        elif servo == 2:
            i2c.write(NEZHA_ADDR, bytearray([0x11, angle, 0, 0]))
        elif servo == 3:
            i2c.write(NEZHA_ADDR, bytearray([0x12, angle, 0, 0]))
        elif servo == 4:
            i2c.write(NEZHA_ADDR, bytearray([0x13, angle, 0, 0]))

