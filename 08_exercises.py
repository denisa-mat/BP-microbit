'''
Úloha 1 - Semafor

Vytvořte funkci, která rozsvítí diody jako na semaforu.
Zvolte vhodnou délku svícení diod. Metodu poté zavolejte
a opakujte desetkrát. K opakování použijte for cyklus.

'''

from microbit import *
from led import *

red_diod = LED(J1)
yellow_diod = LED(J2)
green_diod = LED(J3)

def switch_on_traffic_lights() -> None:
    sleep_time = 2000

    red_diod.set_led_on()
    sleep(sleep_time)
    red_diod.set_led_off()
    yellow_diod.set_led_on()
    sleep(sleep_time/2)
    yellow_diod.set_led_off()
    green_diod.set_led_on()
    sleep(sleep_time)
    green_diod.set_led_off()
    yellow_diod.set_led_on()
    sleep(sleep_time/2)
    yellow_diod.set_led_off()

for _ in range(10):
    switch_on_traffic_lights()


'''
Úloha 2 - SOS

Napište funkci, která bude blikat SOS v Morseově abecedě.
Nezapomeňte, že uvnitř funkce můžete volat jiné funkce.
Nejprve napište funkci pro jeden znak, která bude brát jako
parametr délku jednoho znaku v milisekundách. Dále vytvořte
funkce pro obě potřebná písmena a teprve potom pro celý
signál SOS.
'''

from microbit import *
from led import *

led_diod = LED(J1)

def dot_or_dash(pause_time: int) -> None:
    led_diod.set_led_on()
    sleep(pause_time)
    led_diod.set_led_off()
    sleep(800)

def morse_S() -> None:
    for _ in range(3):
        dot_or_dash(200)

def morse_O() -> None:
    for _ in range(3):
        dot_or_dash(500)

def morse_SOS() -> None:
    morse_S()
    sleep(1000)
    morse_O()
    sleep(1000)
    morse_S()

morse_SOS()
