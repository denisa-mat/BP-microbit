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
## Prostředky - teoretická část 
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
## Úloha 1 - 
### Zadání
### Popis řešení
### Doplňující poznámky 
...
<a name="assignment2"/>
## Úloha 2 - 
### Zadání
### Popis řešení
### Doplňující poznámky 
...
<a name="conclusion"/>
## Shrnutí 
...
<a name="pozn"/>
## Poznámky pro učitele 
