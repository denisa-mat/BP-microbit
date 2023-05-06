# Lekce 5
### For cyklus
## Obsah
[Motivace](#motivace)    
[Prostředky I - For cyklus](#resources2)  
[Úloha 1 - For cykly ](#assignment2)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Cykly obecně umožňují značně zkrátit kód. Vše, co bychom jinak museli psát několikrát lze cyklem zopakovat třeba milionkrát nebo pracovat se vstupy a situacemi různé, předem neznámé délky. Pokud bychom programy, které jsme již vytvořili neměli obalené v nekonečném cyklu, provedla by se pouze jedna iterace a program by skončil. Cykly umožňují programátorům snadno implementovat opakující se procesy a zpracovat velké množství dat pomocí malého množství kódu.

## Prostředky II – For cyklus <a name="resources2"/>
For cyklus je další základní typ cyklu v programování, který slouží k procházení prvků v určité sekvenci, např. v seznamu, řetězci nebo množině, a opakování určitého bloku kódu pro každý prvek v této sekvenci. Tento cyklus se používá tam, kde známe předem počet opakování, nebo je potřeba provádět operace s každým prvkem v dané sekvenci.

Syntaxe for cyklu s daným rozsahem v Pythonu vypadá následovně:
```python
for prvek in range(0, 5):
	# blok kódu, který se opakuje, dokud je podmínka pravdivá
	# lze zde pracovat s promennou, ktera je aktualne v promenne prvek, napriklad:
	print(prvek) # do terminalu postupne vypise hodnoty 0, 1, 2, 3, 4
```
Funkce `range()`, bere hodnoty typu `int`, první číslo značí ostrý počátek intervalu (tedy včetně), druhé konec intervalu (pro zadanou hodnotu se již cyklus nevykoná). Je možné zadat ještě třetí parametr typu `int`, který umožňuje definovat krok. Pokud s proměnnou označující aktuální hodnotu nepotřebujeme pracovat místo názvu dáme `_`. 
## Úloha 1 - For cykly <a name="assignment2"/>
### Zadání
Úloha má tři části, každá část je jeden drobný úkol, zadání proto bude očíslované 1, 2, 3.
1. Napište program, který rozsvítí na matrix modulu postupně všechny diody. Začněte na indexu nula a skončete na indexu 127.
2. Napište program, který rozsvítí na matrix modulu postupně každou třetí diodu (první bude svítit druhá a třetí ne, čtvrtá zase ano).
3. Napište program, který na matrix modulu vytvoří rozsvícením diod šachovnici.
### Co budete potřebovat
Úloha je vytvořena pro maticový displej 8x16 bodů.
### Co se naučíte
Žáci si na jednotlivých úlohách vyzkouší různé varianty for cyklu.
### Jak postupovat
První dva úkoly jsou velmi podobné, nechte žáky se zamyslet v čem se liší a zjistit, co můžeme dát metodě `set_matrix_draw_index`. V třetím úkolu jde o zanoření dvou cyklů, pokud žáci zvládnou bez problému vyřešit první dva úkoly neměl by jim ani tento činit zásadní problémy. vysvětlete operaci modulo, která se pro tuto úlohu velmi hodí. Byť z matematiky žáci pravděpodobně neznají tento název, jedná se vlastně o zbytek po dělení. V informatice jde o velmi užitečnou a často používanou operaci. Celá část se zahodí a vrátí se pouze zbytek. Operaci modulo značíme symbolem procenta `%`. Hlídejte, aby si žáci při párovém programování ve svých dvojicích pravidelně střídali role.
### Vzorová implementace
1.     
```python
from microbit import *
from matrix import *

matrix = MATRIX()

for i in range(0, 128):
    matrix.set_matrix_draw_index(i)
    sleep(100)
	
```
2. 
```python
from microbit import *
from matrix import *

matrix = MATRIX()

for i in range(0, 128, 3):
    matrix.set_matrix_draw_index(i)
    sleep(100)
```
3. 
```python
from microbit import *
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
Naimportujeme modul pro maticový displej, stejně jako v předchozích lekcích. Následně 
### Doplňující poznámky 
Zkuste experimentovat se složením dvojic. Je obvyklou praxí vytvářet páry nevyvážené, kdy jeden z dvojice je pokročilejší než druhý, tím se vzájemně obohatí.
## Shrnutí <a name="conclusion"/>
TODO
## Poznámky pro učitele <a name="pozn"/>
Více informací o tom, jak funguje for cyklus si můžete přečíst v [dokumentaci Pythonu](https://wiki.python.org/moin/ForLoop).

