'''
Úloha 1 - Seznámení s Nezha kitem, Fibonacciho posloupnost
Použijte program vyvtvořený v minulé lekci a modifikujte ho tak,
aby rozsvítil na matrix modulu diody, jejichž pořadí odpovídá
hodnotám Fibonacciho posloupnosti. Naimportujte modul obsahující
metody a funkce pro matrix display a využijte jeho metodu
set_matrix_draw_index().
'''

from microbit import *
from matrix import *

matrix = MATRIX()

number1 = 0
number2 = 1
sum = number1 + number2

while True:
    matrix.set_matrix_draw_index(sum-1)
    number1 = number2
    number2 = sum
    sum = number1 + number2
    sleep(500)

'''
Vytvořte simulaci parkovacího asistenta. Napište program,
který bude pomocí senzoru pro snímání vzdálenosti hlídat,
jak daleko je překážka a tuto vzdálenost vypíše
na segmentový displej (nixietube). Pokud je vzdálenost
menší než 20, pak rozsviďte červenou led diodu.
'''
from microbit import *
from distance import *
from nixietube import *
from led import *

distance = DISTANCE(J1)
nixietube = NIXIETUBE(J2)
led = LED(J3)

while True:
    dist = (distance.get_distance())//1
    nixietube.set_show_num(int(dist))
    if dist < 20:
        led.set_led_on()
    else:
        led.set_led_off()
    sleep(300)
