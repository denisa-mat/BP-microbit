# Lekce 3 - Podmínky
### if, elif, else, logické operátory

### Obsah
[Motivace](#motivace)  
[Prostředky I – Podmínky](#resources1)  
[Úloha 1 - Parkovací asistent](#assignment1)  
[Prostředky II – Složené podmínky](#resources2)  
[Úloha 2 - Test plnoletosti](#assignment2)  
[Úloha 3 - Horská dráha](#assignment3)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  
<a name="motivace"/>
## Motivace 
Podmínky v programování umožňují řídit programový tok na základě různých vstupů, bez podmínek není program dynamický. Často je potřeba provést nějakou akci jen v případě, že nastala nějaká konkrétní situace, to se bez podmínek nepodaří. Znalost podmínek je základem pro mnoho pokročilých programovacích konceptů, jako jsou cykly a funkce.
<a name="resources1"/>
## Prostředky I - Podmínky
Podmínky se používají k rozhodování, které akce má program vykonat v závislosti na nějakém vstupu nebo stavu. 
Pro zápis podmínky využíváme klíčová slova `if` (pokud), `elif` - zkratka pro else if,  `else` (jinak). Za if a elif následuje podmínka (výraz nebo proměnná typu bool) dle toho, jak se vyhodnotí program pokračuje.

Pokud je podmínka vyhodnocena jako `True` (pravda), program vykoná část kódu, která je podmíněna touto podmínkou. Pokud je podmínka vyhodnocena jako `False` (nepravda), program se posune k další podmínce uvedené za `elif`. Pokud ani jedna z podmínek neplatí a již nenásleduje žádná další, program se posune do bloku `else`, který obsahuje výrazy, které se provedou, pokud neplatí ani jedna z podmínek uvedených v `if` ani v `elif`. Program nemusí obsahovat `else` větev vůbec, pokud v případě nesplnění ani jedné z podmínek nechceme vykonávat nic. Je zde důležité dávat pozor na odsazení, dle odsazení Python rozhodne, který řádek vykonat.

Podmínky v Pythonu mají následující zápis:
```python
from microbit import * 

podminka1 = False
podminka2 = True

if podminka1:
	print("podminka1 splnena")
	# kód, který se vykoná je-li splněna podminka1
elif podminka2:
	print("podminka2 splnena")
	# kód, který se vykoná je-li splněna podminka2
else:
	print("podminky nesplneny")
	# kód který se vykoná není li splněna žádná z předchozích podmínek
# zbytek programu
```
``` mermaid
  graph TD;
      A((Start)) --> B[podminka1 = False, podminka2 = True];
      B --> C{podminka1};
      C -- YES --> D[print 'podminka1 splnena'];
	  D --> E[zbytek programu];
      C -- NO --> F[podminka2];
      F -- YES --> G[print 'podminka2 splnena'];
	  G --> E[zbytek programu];
      F -- NO --> H[else, print 'podminky nesplneny'];
      H --> E[zbytek programu];
      E --> I((Konec));
```

V Pythonu se používají následující operátory pro srovnávání hodnot a výrazů:

- `==` (rovná se): Porovnává, zda jsou dva výrazy rovny.
- `!=` (nerovná se): Porovnává, zda jsou dva výrazy nerovnající se.
- `<` (menší než): Porovnává, zda je první výraz menší než druhý výraz.
- `>` (větší než): Porovnává, zda je první výraz větší než druhý výraz.
- `<=` (menší nebo rovno): Porovnává, zda je první výraz menší nebo roven druhému výrazu.
- `>=` (větší nebo rovno): Porovnává, zda je první výraz větší nebo roven druhému výrazu.
- `in`: Porovnává, zda se první výraz nachází v druhém výrazu (seznamu, řetězci apod.).
- `not in`: Porovnává, zda se první výraz nenachází v druhém výrazu.

## Úloha 1 - Parkovací asistent<a name="assignment1"/>
### Zadání
Vytvořte simulaci parkovacího asistenta TODO
### Co budete potřebovat
TODO
### Co se naučíte
TODO
### Vzorová implementace
```python
from distance import *
from nixietube import *
from led import *

distance = DISTANCE(J1)
nixietube = NIXIETUBE(J2)
led = LED(J3)

to_close_dist = 20

while True:
    dist = (distance.get_distance())//1
    nixietube.set_show_num(int(dist))
    if dist < to_close_dist:
        led.set_led(1, 50)
    else:
        led.set_led(0, 50)
    sleep(300)
```
### Diagram
``` mermaid
  graph TD;
      A((Start)) --> B[to_close_dist = 10];
      B --> C{Is it True?};
      C -- YES --> D[uloz vzdalenost do prom dist];
	  D --> E{dist < to_close_dist};
	  	E -- YES --> G[rozsvit cervenou led];
      E -- NO --> H[vyckej 300 ms];
      G --> H;
      H --> C;
```
### Popis řešení
TODO
### Doplňující poznámky 
TODO
<a name="resources2"/>
## Prostředky II - Složené podmínky
V Pythonu se používají tři logické operátory pro kombinaci podmínek: `and`, `or` a `not`.

Operátor `and` vrací `True`, pokud jsou obě podmínky pravdivé, jinak vrací `False`.
```python
if podmínka1 and podmínka2:
    # provede se, pokud jsou obě podmínky pravdivé
```

Operátor `or` vrací `True`, pokud alespoň jedna z podmínek je pravdivá, jinak vrací `False`.
```python
if podmínka1 or podmínka2:
    # provede se, pokud je alespoň jedna z podmínek pravdivá
```

Operátor `not` neguje pravdivostní hodnotu podmínky, tedy vrací `True`, pokud je podmínka nepravdivá, a `False`, pokud je podmínka pravdivá.
```python
if not podmínka1:
    # provede se, pokud je podmínka1 nepravdivá
```

Tyto logické operátory můžeme využít pro sestavení složitějších podmínek. Operátory a podmínky lze spojovat a pomocí závorek zanořovat, vyhodnocení podmínky začíná u levého nejvíce vnitřního výrazu a pokračuje postupně k vnějším výrazům.

## Úloha 2 - Test plnoletosti "vyhazovač" <a name="assignment2"/>
### Zadání
TODO
### Co budete potřebovat
TODO
### Co se naučíte
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
``` mermaid
  graph TD;
      A((Start)) --> B[age = 0];
      B --> C[age_confirmed = False];
      C --> D{True};
      D -- YES --> E{age_confirmed?};
	  E -- YES --> G{age < 5};
		G -- YES --> H[vykresli na displej Image.Sad];
		 H --> Q[vypis age na segmentovy displej];
		G --> NO --> I{age < 18};
			I -- YES --> J[vykresli na displej Image.NO];
				J --> Q;
			        Q --> D;
			I -- NO --> K[vykresli na displej Image.YES];
				K --> Q;
          E -- NO --> L{je button C stisknut?};
	  	L -- YES --> M[age += 1];
		 M --> N[vyckej 300 ms];
		 N --> Q;
		L -- NO --> O{je button D stisknut?};
			O -- YES --> P[age_confirmed = True];
      		  	 P --> Q;
			O -- NO --> Q
```
### Popis řešení
TODO
### Doplňující poznámky 
TODO

## Úloha 3 - Horská dráha <a name="assignment3"/>
### Zadání
TODO
### Co budete potřebovat
TODO
### Co se naučíte
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

