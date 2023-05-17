'''
Úloha 1 - Auto

Sestavte ze Nezha sady vozidlo, které bude pohánět motor
a v předu bude mít distance senzor a crash senzor. Poté
ho naprogramujte tak, že pojede rychlostí `fast`, dokud
crash senzor nezaznamená náraz. Pokud bude vozidlo překážce
blíže než 40 centimetrů zpomalí na rychlost `slow`. Auto
pojede až do chvíle, než sepne crash senzor, v tu chvíli
se zastaví a program skončí.
'''

from microbit import *
from motor import *
from crash import *
from distance import *

motor = MOTOR(1)
crash = CRASH(J1)
distance = DISTANCE(J2)

while not crash.crash_is_pressed():
    dist = distance.get_distance()
    if dist < 40:
        motor.set_motor_forward_slow()
    else:
        motor.set_motor_forward_fast()
motor.set_motor_stop()


'''
Úloha 2 - Auto vylepšení

Využijte kód z předchozí lekce a modifikujte ho tak, aby
si před startem auto uložilo vzdálenost od překážky
a když narazí, tak aby vycouvalo zpět a zastavilo se
na stejném místě, ze kterého vyjelo. Následně zkuste sami
vymyslet, jak by se dalo ještě auto vylepšit. Přidejte
další modul a naprogramujte nějakou další funkcionalitu.
'''

from microbit import *
from motor import *
from crash import *
from distance import *

motor = MOTOR(1)
crash = CRASH(J1)
distance = DISTANCE(J2)

start_distance = distance.get_distance()

while not crash.crash_is_pressed():
    dist = distance.get_distance()
    if dist < 40:
        motor.set_motor_forward_slow()
    else:
        motor.set_motor_forward_fast()
motor.set_motor_stop()

while start_distance > distance.get_distance():
    motor.set_motor_backward_slow()
motor.set_motor_stop()
