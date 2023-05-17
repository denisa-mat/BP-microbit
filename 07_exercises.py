'''
Úloha 1 - Seznamy

Vytvořte vhodně pojmenovaný seznam délky, kterou
si definujete v proměnné. Do seznamu pomocí
`random.randint()` náhodně vygenerujte znaky "C"
a "D". Poté nový seznam postupně zobrazte
na displej micro:bitu.
'''

from microbit import *
from random import randint

memory_test_size = 6
memory_list = []

for _ in range(memory_test_size):
    random_value = randint(0,2)
    if random_value == 0:
        memory_list.append("C")
    else:
        memory_list.append("D")

for value in memory_list:
    display.scroll(value)


'''
Úloha 2 - Memory test

Úkolem je napsat program, který bude simulovat test paměti.
V minulé úloze jste si nachystali náhodné generování seznamu.
Nyní budete ověřovat, zda si uživatel zapamatoval sekvenci
správně. Uživatel bude mačkat tlačítka z modulu button
(označená C, D) v zobrazeném pořadí. Pokud zadá správně
rozsvítí se červená LED dioda, pokud špatně tak zelená.
Na konci programu se zobrazí na micro:bit emoji. V případě,
že byla celá sekvence správně, zobrazte `Image.HAPPY`, jinak
`Image.SAD`.
'''

from microbit import *
from button import *
from led import *
from random import randint

button = BUTTON(J1)
green_led = LED(J2)
red_led = LED(J3)

memory_test_size = 6
memory_list = []

for _ in range(memory_test_size):
    random_value = randint(0,2)
    if random_value == 0:
        memory_list.append("C")
    else:
        memory_list.append("D")

for value in memory_list:
    display.scroll(value)

input_list = []

C_was_pressed = False
D_was_pressed = False
    
for i in range(memory_test_size):
    while not C_was_pressed and not D_was_pressed:
        C_was_pressed = button.C_is_pressed()
        D_was_pressed = button.D_is_pressed()
        
    if C_was_pressed:
        input_list.append("C")
    elif D_was_pressed:
        input_list.append("D")
        
    if memory_list[i] == input_list[i]:
        green_led.set_led_on()
    else:
        red_led.set_led_on()
        
    sleep(600)
    C_was_pressed = False
    D_was_pressed = False
    red_led.set_led_off()
    green_led.set_led_off()
    
if memory_list == input_list:
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)
