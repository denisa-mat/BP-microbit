"""
Úloha 1 - Proměnné, Fibonacciho posloupnost

Napište program, který bude v nekonečném cyklu while True počítat Fibonaccioho
posloupnost a vypisovat její výpočet na micro:bit (použijte metodu scroll
obdobně jako v minulé lekci). Program bude obsahovat tři proměnné – dva 
sčítance a výsledek. Proměnné vhodně pojmenujte. První výpis bude vypadat 
následovně: 0+1=1
"""

from microbit import * 

number1 = 0
number2 = 1   

while True:   
    sum = number1 + number2     
    display.scroll(str(number1) + "+" + str(number2) + "=" + str(sum))
    number1 = number2
    number2 = sum


"""
Úloha 2 - Seznámení s Nezha kitem, Fibonacciho posloupnost

Použijte již vytvořený program a modifikujte ho tak, aby rozsvítil na 
matrix modulu diody, jejichž pořadí odpovídá hodnotám Fibonacciho posloupnosti.
Naimportujte modul obsahující metody a funkce pro matrix display a využijte 
jeho metodu set_matrix_draw_index().
"""
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