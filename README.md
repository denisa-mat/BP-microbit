# Lekce 4
### While cyklus, for cyklus

## Obsah
[Motivace](#motivace)  
[Prostředky I - While cyklus](#resources1)  
[Úloha 1 - ](#assignment1)  
[Prostředky II - For cyklus](#resources2)  
[Úloha 2 - ](#assignment2)  
[Úloha 3 - ](#assignment3)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Cykly obecně umožňují značně zkrátit kód, vše co bychom jinak museli psát opakovaně lze cyklem zopakovat třeba milionkrát nebo pracovat se vstupy/situacemi různé, předem neznámé délky. Pokud bychom programy, které jsme již vytvořili neměli obalené v nekonečném cyklu, provedla by se pouze jedna iterace a program by skončil. Cykly umožňují programátorům snadno implementovat opakující se procesy a zpracovat velké množství dat pomocí malého množství kódu.
## Prostředky I - While cyklus <a name="resources1"/>
While cyklus využívá podmínky, čímž plynule navazuje na předchozí lekci. Má také podobnou syntax. While cyklus se používá k řešení situací, kdy nevíme přesně, kolikrát bude třeba provést určitou akci. Smyslem cyklů je opakování zanořeného bloku kódu, dokud je podmínka splněna. Není-li podmínka splněna již v první iteraci, blok kódu se vůbec nevykoná.
Zápis while cyklu vypadá následovně:
```python
while podmínka:
    # blok kódu, který se opakuje, dokud je podmínka pravdivá
# blok kódu, kde program pokračuje, když podmínka není pravdivá
```
I u cyklů je důležité dávat pozor na správné odsazení, bez toho nebude program fungovat správně.
Přestože jsme dosud pro zjednodušení používali nekonečný cyklus `while True`, od této chvíle je to něco, čemu se budeme chtít spíš vyhnout. Každý porgram má nějaký konečný stav v němž chceme aby skončil.
## Úloha 1 - Proměnné <a name="assignment1"/>
### Zadání
TODO
### Co budete potřebovat
TODO
### Co se naučíte
TODO
### Vzorová implementace
```python
#from microbit import *
from nezha import *
from crash import *
from distance import *

nezha = NEZHA()
crash = CRASH(J1)
distance = DISTANCE(J2)

nezha.set_motors(3, -100)

while not crash.crash_is_pressed():
    dist = distance.get_distance()
    if dist < 40:
       nezha.set_motors(3, -20)
    else:
        nezha.set_motors(3, -100)
nezha.set_motors(3, 0)


#do poznamky vysvetlit proc else vetev
```

### Popis řešení
TODO
### Doplňující poznámky 
TODO
## Prostředky II -  <a name="resources2"/>
TODO
## Úloha 2 - <a name="assignment3"/>
### Zadání
TODO
### Co budete potřebovat
TODO
### Co se naučíte
TODO
### Vzorová implementace
```python
from microbit import * 

#TODO
```

### Popis řešení
TODO
### Doplňující poznámky 
TODO
## Shrnutí <a name="conclusion"/>
TODO
## Poznámky pro učitele <a name="pozn"/>
TODO

