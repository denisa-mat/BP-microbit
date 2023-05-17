'''
Úloha 1 - Test plnoletosti

Napište program, který bude kontrolovat věk osoby zadaný pomocí
modulu `button`. Když se stiskne `button C` přičte se jeden rok
až dokud není zmáčknut `button D`, kterým se věk potvrdí.
Po celou dobu zobrazujte aktuální věk na segmentovém displeji
(`nixietube`). Pokud je věk potvrzen a osoba je mladší pěti let,
zobrazte smutného smajlíka (`Image.SAD`). Pokud je mladší než
osmnáct, zobrazte křížek (`Image.NO`), pokud už osoba dosáhla
osmnácti let zobrazte fajfku (`Image.YES`).
'''

from microbit import *
from distance import *
from nixietube import *
from button import *

nixietube = NIXIETUBE(J1)
button = BUTTON(J2)

age = 0
age_confirmed = False

while True:
    if age_confirmed:
        if age < 5:
            display.show(Image.SAD)
        elif age < 18:
            display.show(Image.NO)
        else:
            display.show(Image.YES)
    else:
        if button.C_is_pressed():
            age += 1
            sleep(300)
        elif button.D_is_pressed():
            age_confirmed = True
    nixietube.set_show_num(age)


'''
Úloha 2 - Horská dráha

Naprogramujte micro:bita, tak aby na displej zobrazoval, zda
může zájemce jít na horskou dráhu. Na horskou dráhu může
zájemce jen, pokud je mu alespoň 11 let nebo měří více než
125 centimetrů. Zkuste pro řešení využít kód z předcházející
úlohy, věk a výška se bude načítat stejným způsobem, jako věk
v předchozí úloze.
'''

from microbit import *
from nixietube import *
from button import *

nixietube = NIXIETUBE(J1)
button = BUTTON(J2)

age = 0
age_confirmed = False
height = 0
height_confirmed = False

while True:
    if age_confirmed and height_confirmed:
        if age <= 10 and height < 125:
            display.show(Image.NO)
        else:
            display.show(Image.YES)
    elif age_confirmed:
        if button.C_is_pressed():
            height += 5
            nixietube.set_show_num(height)
        elif button.D_is_pressed():
            height_confirmed = True
            nixietube.set_clear()
    else:
        if button.C_is_pressed():
            age += 1
            nixietube.set_show_num(age)
        elif button.D_is_pressed():
            age_confirmed = True
            nixietube.set_clear()
    sleep(150)
