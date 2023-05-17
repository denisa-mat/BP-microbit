'''
Úloha 1 - Honzův zkouškový úkol

Student Honza se zúčastnil zkoušky a měl za úkol splnit následující zadání.
1. Vytvořte parametrickou funkci na výpočet faktoriálu.
2. Výsledek pro čísla v rozmezí 0-7 včetně postupně zobrazte na segmentový displej. Pro opakování použijte while cyklus.

Honza ale nechodil na přednášky. A tak tam má spoustu chyb. Vaším úkolem je chyby najít.
Postupujte postupně:
1. Kód zanalyzujte a pokuste se najít co nejvíce chyb. Nalezené či domnělé chyby si zapište.
2. Kód přepište do editoru a opravte v něm nalezené chyby.
3. Kód spusťte a ověřte si, jak se vám podařilo chyby odhalit.
4. Kód se pokuste opravit.
'''

#Implementace k opraveni

from microbit import * 

def factorial(number: int) -> int:
    if number < 0:
        return -1
    if number == 0:
       return 1

    factorial_result = 0

    for i in range(number):
        factorial_result * i

    return factorial_result

number = 0

while number < 7:
    fact = factorial(0, 7)
    #TODO: zobraz vysledek na segmentovy displej


# Jak muze vypadat oprava

from microbit import * 
from nixietube import *
from led import *

nixietube_display = NIXIETUBE(J1)

def factorial(number: int) -> int:
    if number < 0:
        return -1
    elif number == 0:
        return 1

    factorial_result = 1

    for i in range(1, number + 1):
        factorial_result = factorial_result * i

    return factorial_result

number = 0

while number < 8:
    fact = factorial(number)
    nixietube_display.set_show_num(fact)
    sleep(2000)
    number += 1


'''
Úloha 2 - Větrák

Sestavte si větráček, poháněný motorem. Rychlost motoru bude ovládaná pomocí potenciometru (trimpot). 
Následně se pokuste opravit kód níže a zprovoznit větrák.
'''

#Implementace k opraveni

from microbit import *
from motor import *
from trimpot import *

motor = MOTOR(1)
trimpot = TRIMPOT(J1)

fan_setting()

def fan_setting():
    while button_a.is_pressed():
        #vypocet hodnoty speed je korektni
        speed = int((trimpot.get_trimpot_value()/1023)*100)
        motor.set_motor(sped)
    motor.stop()


# Jak muze vypadat oprava

from microbit import *
from motor import *
from trimpot import *

motor = MOTOR(1)
trimpot = TRIMPOT(J1)

def fan_setting():
    while not button_a.is_pressed():
        #vypocet hodnoty speed je korektni
        speed = int((trimpot.get_trimpot_value()/1023)*100)
        motor.set_motor(speed)
    motor.set_motor_stop()

fan_setting()