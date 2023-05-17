'''
 Úloha 1 - For cykly

Úloha má tři části, každá část je jeden drobný úkol, zadání proto bude očíslované.
1. Napište program, který rozsvítí na matrix modulu postupně všechny diody. Začněte na indexu nula a skončete na indexu 127.
2. Napište program, který rozsvítí na matrix modulu postupně každou třetí diodu (první bude svítit druhá a třetí ne, čtvrtá zase ano).
3. Napište program, který na matrix modulu vytvoří rozsvícením diod šachovnici.
'''

#1.     
from microbit import *
from matrix import *

object_matrix = MATRIX()

for i in range(0, 128):
    object_matrix.set_matrix_draw_position(i)
    sleep(100)


#2. 
from microbit import *
from matrix import *

object_matrix = MATRIX()

for i in range(0, 128, 3):
    object_matrix.set_matrix_draw_position(i)
    sleep(100)

#3. 
from microbit import *
from matrix import *

object_matrix = MATRIX()

for column in range(0, 16):
    for row in range (0, 8):
        if (column % 2 == 0) and (row % 2 == 0):
            object_matrix.set_matrix_draw(column, row)
        elif (column % 2 == 1) and (row % 2 == 1):
            object_matrix.set_matrix_draw(column, row)



'''
Úloha 2 - Odpočet

Napište program, který bude simulovat start závodu. Nejprve rozsviťte červenou diodu. Poté pomocí 
for cyklu vypište na displej micro:bitu čísla 3, 2, 1 a následně rozsviťte zelenou diodu.
'''
from microbit import *
from led import *

red_led_object = LED(J1)
green_led_object = LED(J2)

red_led_object.set_led_on()

for i in range(3):  
    display.scroll(3-i)

red_led_object.set_led_off()
green_led_object.set_led_on()
