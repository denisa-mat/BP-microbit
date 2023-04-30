# Lekce 3 - Podmínky
### if, elif, else, logické operátory

### Obsah
[Motivace](#motivace)  
[Prostředky](#resources)  
[Úloha 1](#assignment1)  
[Úloha 2](#assignment2)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  
<a name="motivace"/>
## Motivace 
Podmínky v programování umožňují řídit programový tok na základě různých vstupů, bez podmínek není program dynamický. Často je potřeba provést nějakou akci jen v případě, že nastala nějaká konkrétní situace, to se bez podmínek nepodaří. Znalost podmínek je základem pro mnoho pokročilých programovacích konceptů, jako jsou cykly a funkce.
<a name="resources"/>
## Prostředky - Podmínky 
Podmínky se používají k rozhodování, které akce má program vykonat v závislosti na nějakém vstupu nebo stavu. Pokud je podmínka vyhodnocena jako true, program vykoná nějakou část kódu, která je podmíněna touto podmínkou. Pokud je podmínka vyhodnocena jako false, program pokračuje za podmíněnou částí kódu, případně skončí, pokud následuje konec programu. Pro zápis jednoduché podmínky využíváme klíčová slova if (pokud) a else (jinak). Za if následuje výraz nebo proměnná typu bool. Vyhodnotí-li se výraz jako true vykoná se kód následující pod if, pokud se vyhodnotí jako false vykoná se program následující za else. Zde je důležité dávat pozor na odsazení, dle odsazení Python rozhodne, který řádek vykonat. 
Podmínky v Pythonu mají následující zápis:
```python
from microbit import * 

choosen_number = 5
if choosen_number != 0:
	display.scroll(str(choosen_number) + "není 0")
	result = 100 // choosen_number
else
	display.scroll(str(choosen_number) + "je 0")
# tady následuje zbytek programu
```
TODO algoritmus - graficky
<a name="assignment1"/>
## Úloha 1 - Parkovací asistent
### Zadání
TODO
### Vzorová implementace
```python
from microbit import *
from distance import *
from nixietube import *
import music

nixietube = NIXIETUBE(J2)
distance = DISTANCE(J1)

to_close_dist = 10

while True:
    dist = (distance.get_distance())//1
    nixietube.set_show_num(int(dist))
    if dist < to_close_dist:
        music.play(music.BA_DING)
    sleep(300)
```
### Popis řešení
TODO
### Doplňující poznámky 
TODO
<a name="assignment2"/>
## Úloha 2 - Test plnoletosti "vyhazovač"
### Zadání
TODO
### Vzorová implementace
```python
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
```
### Popis řešení
TODO
### Doplňující poznámky 
TODO
## Úloha 3 - Horská dráha
### Zadání
TODO
### Vzorová implementace
```python
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
        if age < 5:
            display.show(Image.SAD)
        elif age <= 10 and height < 125:
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
```
### Popis řešení
TODO
### Doplňující poznámky 
TODO
<a name="conclusion"/>
## Shrnutí 
TODO
<a name="pozn"/>
## Poznámky pro učitele 
TODO
