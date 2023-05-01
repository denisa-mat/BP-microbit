# Lekce 4
### While cyklus, for cyklus

## Obsah
[Motivace](#motivace)  
[Prostředky I - While cyklus](#resources1)  
[Úloha 1 -  Auto](#assignment1)  
[Prostředky II - For cyklus](#resources2)  
[Úloha 2 - For cykly ](#assignment2)  
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
## Úloha 1 - Auto <a name="assignment1"/>
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

nezha.set_motor(3, -100)

while not crash.crash_is_pressed():
    dist = distance.get_distance()
    if dist < 40:
       nezha.set_motor(3, -20)
    else:
        nezha.set_motors(3, -100)
nezha.set_motors(3, 0)

#do poznamky vysvetlit proc else vetev
```

### Popis řešení
TODO
### Doplňující poznámky 
TODO
## Prostředky II - For cyklus <a name="resources2"/>
For cyklus je další základní typ cyklu v programování, který slouží k procházení prvků v určité sekvenci, např. v seznamu, řetězci nebo množině, a opakování určitého bloku kódu pro každý prvek v této sekvenci. Tento cyklus se používá tam, kde známe předem počet opakování, nebo je potřeba provádět operace s každým prvkem v dané sekvenci.

Syntaxe for cyklu s daným rozsahem v Pythonu vypadá následovně:
```python
for prvek in range(0, 5):
	# blok kódu, který se opakuje, dokud je podmínka pravdivá
	# lze zde pracovat s promennou, ktera je aktualne v promenne prvek, napriklad:
	print(prvek) # do terminalu postupne vypise hodnoty 0, 1, 2, 3, 4
```
Funkce `range()`, bere hodnoty typu `int`, první číslo značí ostrý počátek intervalu (tedy včetně), druhé konec intervalu (pro zadanou hodnotu se již cyklus nevykoná). Je možné zadat ještě třetí parametr typu `int`, který umožňuje definovat krok. Pokud s proměnnou označující aktuální hodnotu nepotřebujeme pracovat místo názvu dáme `_`. 
## Úloha 2 - For cykly <a name="assignment2"/>
### Zadání
Úloha má tři části, každá část je jeden drobný úkol, zadání proto bude očíslované 1, 2, 3.
1. Napište program, který rozsvítí na matrix modulu postupně všechny diody. Začněte na idexu nula a skončete na indexu 127.
2. Napište program, který rozsvítí na matrix modulu postupně každou třetí diodu (první bude svítit druhá a třetí ne, čtvrtá zase ano).
3. Napište program, který na matrix modulu vytvoří rozsvícením diod šachovnici.
### Co budete potřebovat
Matrix modul
### Co se naučíte
TODO
### Vzorová implementace
1.     
```python
from matrix import *

matrix = MATRIX()

for i in range(0, 128):
    matrix.set_matrix_draw_index(i)
    sleep(100)
	
```
2. 
```python
from matrix import *

matrix = MATRIX()

for i in range(0, 128, 3):
    matrix.set_matrix_draw_index(i)
    sleep(100)
```
3. 
```python
from matrix import *

matrix = MATRIX()

for row in range(0, 16):
    for column in range (0, 8):
        if (row % 2 == 0) and (column % 2 == 0):
            matrix.set_matrix_draw(row, column)
        elif (row % 2 == 1) and (column % 2 == 1):
            matrix.set_matrix_draw(row, column)
```

### Popis řešení
TODO
### Doplňující poznámky 
TODO
## Shrnutí <a name="conclusion"/>
TODO
## Poznámky pro učitele <a name="pozn"/>
TODO

