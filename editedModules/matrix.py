from microbit import *

HT16K33_ADDRESS = 0x70

HT16K33_BLINK_CMD = 0x80

HT16K33_BLINK_DISPLAYON = 0x01

HT16K33_CMD_BRIGHTNESS = 0xE0


class MATRIX(object):
    """
    8x16 matrix display class

    """

    def __init__(self):
        i2c.init()
        self.__initmodule()
        self.__matBuf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __i2cwrite_matrix(self, addr, reg):
        i2c.write(addr, bytearray([reg]))

    def __initmodule(self):
        self.__i2cwrite_matrix(HT16K33_ADDRESS, 0x21)
        self.__i2cwrite_matrix(HT16K33_ADDRESS, HT16K33_BLINK_CMD | HT16K33_BLINK_DISPLAYON | (0 << 1))
        self.__i2cwrite_matrix(HT16K33_ADDRESS, HT16K33_CMD_BRIGHTNESS | 0xF)

    def __matrix_show(self):
        """
        performs the lighting up
        Params:
            NONE

        Returns:
            NONE
        """
        self.__matBuf[0] = 0x00
        i2c.write(HT16K33_ADDRESS, bytearray([
            self.__matBuf[0], self.__matBuf[1], self.__matBuf[2], self.__matBuf[3], self.__matBuf[4], self.__matBuf[5],
            self.__matBuf[6], self.__matBuf[7], self.__matBuf[8], self.__matBuf[9], self.__matBuf[10],
            self.__matBuf[11],
            self.__matBuf[12], self.__matBuf[13], self.__matBuf[14], self.__matBuf[15], self.__matBuf[16]]))

    def set_matrix_clear(self):
        """
        clears the matrix
        Params:
            NONE

        Returns:
            NONE
        """
        for i in range(17):
            self.__matBuf[i] = 0
        self.__matrix_show()

    def set_matrix_draw(self, x, y):
        """
        ligths up diod on given coordinates
        Params:
            x (int): index on x axis, valid values in range 0-15
            y (int): index on y axis, valid values in range 0-7

        Returns:
            NONE
        """
        if 0 > x > 15:
            raise ValueError('x error, <0,15>')
        if 0 > y > 7:
            raise ValueError('y error, <0,7>')
        idx = int(y) * 2 + int(x) // 8
        tmp = self.__matBuf[idx + 1]
        tmp |= (1 << (x % 8))
        self.__matBuf[idx + 1] = tmp
        self.__matrix_show()

    def set_matrix_draw_position(self, position):
        """
        ligths up diod on given position, consider the matrix as line
        Params:
            position (int): position on the line, valid values in range 1-128

        Returns:
            NONE
        """
        if 1 > positon > 128:
            raise ValueError('position error, <1,128>')
        x = (position-1) % 16
        y = (position-1) // 16
        print(x, y)
        self.set_matrix_draw(x, y)

    def set_matrix_expression(self, emoji):
        """
        shows given expression, if expression unknown show nothing
        Params:
            emoji (str): valid values Neutral, Sad, Smile, Angry

        Returns:
            NONE
        """
        point = []
        if expression == "Neutral":
            point = [[2, 1], [3, 1], [13, 1], [12, 1],
                     [2, 2], [3, 2], [13, 2], [12, 2],
                     [2, 3], [3, 3], [13, 3], [12, 3],
                     [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5],
                     [5, 6], [6, 6], [7, 6], [8, 6], [9, 6], [10, 6]
                     ]
        elif expression == "Sad":
            point = [[1, 2], [5, 2], [10, 2], [14, 2],
                     [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [10, 3], [11, 3], [12, 3], [13, 3], [14, 3],
                     [2, 4], [3, 4], [4, 4], [11, 4], [12, 4], [13, 4],
                     [6, 6], [7, 6], [8, 6], [9, 6],
                     [5, 7], [10, 7]
                     ]
        elif expression == "Smile":
            point = [[2, 1], [3, 1], [13, 1], [12, 1],
                     [2, 2], [3, 2], [13, 2], [12, 2],
                     [2, 3], [3, 3], [13, 3], [12, 3],
                     [5, 5], [10, 5],
                     [6, 6], [7, 6], [8, 6], [9, 6]
                     ]
        elif expression == "Angry":
            point = [[2, 0], [13, 0],
                     [3, 1], [12, 1],
                     [3, 2], [4, 2], [11, 2], [12, 2],
                     [3, 3], [4, 3], [11, 3], [12, 3],
                     [6, 6], [7, 6], [8, 6], [9, 6],
                     [5, 7], [10, 7]
                     ]
        else:
            raise ValueError('unknown emoji')
        self.set_matrix_clear()
        for i in range(len(point)):
            self.set_matrix_draw(point[i][0], point[i][1])
