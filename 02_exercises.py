'''
Úloha 1 - Proměnné, výpis

Napište program, na jehož začátku do proměnných uložíte vaše jméno
a věk a následně zobrazte postupně na displej text ve tvaru
`Vase jmeno je Anonym a vek je 99 let.`
'''

from microbit import *

name = "Anonym"
age = 99

display.show("Vase jmeno je " + name + " a vek je " +
             str(age) + " let.")


"""
Úloha 2 - Proměnné, Fibonacciho posloupnost

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
