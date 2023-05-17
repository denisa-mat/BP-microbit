from microbit import *

NEZHA_ADDR = 0x10

class MOTOR(object):
    """
    motor module class

    Params:
        motor_pin: 1, 2, 3, 4

    """
    def __init__(self, motor_pin):
        if motor_pin not in [1, 2, 3, 4]:
            raise ValueError("motor_pin must be in [1, 2, 3, 4]")
        i2c.init()
        self.__pin__ = motor_pin
        self.__speed__ = 0
        self.__goes_forward__ = False
        
    def set_motor(self, speed: int) -> None:
        """
        sets speed
        Params:
            speed (int): valid values within -100~100

        Return: NONE
        """
        if speed > 100 or speed < -100:
            raise ValueError('speed error, <-100, 100>')

        if speed < 0:
            i2c.write(NEZHA_ADDR, bytearray([self.__pin__, 0x02, speed * -1, 0]))
            self.__goes_forward__ = False
            self.__speed__ = speed * -1
        else:
            i2c.write(NEZHA_ADDR, bytearray([self.__pin__, 0x01, speed, 0]))
            self.__goes_forward__ = True
            self.__speed__ = speed


    def set_motor_forward_slow(self) -> None:
        """
        sets speed to slow, 20
        Params: NONE

        Return: NONE
        """
        self.set_motor(20)

    def set_motor_forward_fast(self) -> None:
        """
        sets speed to fast, 60
        Params: NONE

        Return: NONE
        """
        self.set_motor(60)

    def set_motor_forward_very_fast(self) -> None:
        """
        sets speed to fast, 100
        Params: NONE

        Return: NONE
        """
        self.set_motor(100)

    def set_motor_stop(self) -> None:
        """
        sets motor off, sets speed to 0
        Params: NONE

        Return: NONE
        """
        self.set_motor(0)

    def set_motor_backward_slow(self) -> None:
        """
        sets motor to go backward with slow speed, -20
        Params: NONE

        Return: NONE
        """
        self.set_motor(-20)

    def set_motor_backward_fast(self) -> None:
        """
        sets motor to go backward with fast speed, -60
        Params: NONE

        Return: NONE
        """
        self.set_motor(-60)

    def set_motor_backward_very_fast(self) -> None:
        """
        sets motor to go backward with very fast speed, -100
        Params: NONE

        Return: NONE
        """
        self.set_motor(-100)

    def get_motor_speed(self) -> int:
        """
        returns positive motor speed
        Params: NONE

        Return: (int), speed
        """
        return self.__speed__

    def get_motor_goes_forward(self) -> bool:
        """
        returns True if motor goes forward, False otherwise
        Params: NONE

        Return: (int), speed
        """
        return self.__goes_forward__
