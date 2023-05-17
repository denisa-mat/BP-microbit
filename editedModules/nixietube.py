from microbit import *
from enum import *

TM1637_CMD1 = 64  # 0x40 data command
TM1637_CMD2 = 192  # 0xC0 address command
TM1637_CMD3 = 128  # 0x80 display control command

_SEGMENTS = (0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F, 0x77, 0x7C, 0x39, 0x5E, 0x79, 0x71)


class NIXIETUBE(object):
    """
    7-Seg LED Nixie tube class

    """

    def __init__(self, RJ_pin, intensity=7, number=4):
        if RJ_pin == J1:
            self.__clk = pin1
            self.__dio = pin8
        elif RJ_pin == J2:
            self.__clk = pin2
            self.__dio = pin12
        elif RJ_pin == J3:
            self.__clk = pin13
            self.__dio = pin14
        elif RJ_pin == J4:
            self.__clk = pin15
            self.__dio = pin16

        self.__intensity = intensity % 8
        self.__LED = number
        self.__ON = 8
        self.__buf_d = [0, 0, 0, 0]

        self.__clk.write_digital(0)
        self.__dio.write_digital(0)

        self.set_clear()

    def __start(self):
        self.__dio.write_digital(0)
        self.__clk.write_digital(0)

    def __stop(self):
        self.__dio.write_digital(0)
        self.__clk.write_digital(1)
        self.__dio.write_digital(1)

    def __write_data_cmd(self):
        self.__start()
        self.__write_byte(TM1637_CMD1)
        self.__stop()

    def __write_dsp_ctrl(self):
        self.__start()
        self.__write_byte(TM1637_CMD3 | self.__ON | self.__intensity)
        self.__stop()

    def __write_byte(self, b):
        for i in range(8):
            self.__dio.write_digital((b >> i) & 1)
            self.__clk.write_digital(1)
            self.__clk.write_digital(0)
        self.__clk.write_digital(1)
        self.__clk.write_digital(0)

    def __dat(self, bit, dat):
        self.__write_data_cmd()
        self.__start()
        self.__write_byte(TM1637_CMD2 | (bit % self.__LED))
        self.__write_byte(dat)
        self.__stop()
        self.__write_dsp_ctrl()

    def set_power_on(self) -> None:
        """
        sets display on

        """
        self.__ON = 8
        self.__write_data_cmd()
        self.__write_dsp_ctrl()

    def set_power_off(self) -> None:
        """
        sets display off

        """
        self.__ON = 0
        self.__write_data_cmd()
        self.__write_dsp_ctrl()

    def set_intensity(self, intensity) -> None:
        """
        sets intensity

        Params:
            intensity (number): intensity, valid within <0,8>
        Return:
            NONE

        """
        intensity = max(0, min(val, 8))
        if intensity == 0:
            self.set_power_off()
        else:
            self.__ON = 8
            self.__intensity = intensity - 1
            self.__write_data_cmd()
            self.__write_dsp_ctrl()

    def set_clear(self) -> None:
        """
        clears nixie tube
        Params:
            NONE
        Return:
            NONE
        """
        self.__dat(0, 0)
        self.__dat(1, 0)
        self.__dat(2, 0)
        self.__dat(3, 0)
        self.__buf_d = [0, 0, 0, 0]

    def set_show_bit(self, num: int, bit=0) -> None:
        """
        shows number on given bit, default is 0

        Params:
            num (int): number to be shown, valid within <0,9>
            bit (int): postion, valid within <0,4>, default 0, optional

        """
        self.__buf_d[bit % self.__LED] = _SEGMENTS[num % 16]
        self.__dat(bit, _SEGMENTS[num % 16])

    def set_show_DP(self, bit=1, show=True) -> None:
        """

        Params:
            bit (int): postion, valid within <0,4>
            show (bool):
        Return:
            NONE

        """
        bit_var = bit % self.__LED
        if show:
            self.__dat(bit_var, self.__buf_d[bit_var] | 0x80)
        else:
            self.__dat(bit_var, self.__buf_d[bit_var] & 0x7F)

    def set_show_num(self, num: int) -> None:
        """
        shows number

        Params:
            num (int): number to be shown, valid within <-999,9999>
        Return:
            NONE

        """
        if num < 0:
            # add the - sign
            self.__dat(0, 0x40)
            num = -num
        else:
            self.set_show_bit((num // 1000) % 10)
        self.set_show_bit(num % 10, 3)
        self.set_show_bit((num // 10) % 10, 2)
        self.set_show_bit((num // 100) % 10, 1)
