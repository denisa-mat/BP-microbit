# Lekce 9
### Testování

## Obsah
[Motivace](#motivace)  
[Prostředky I - ](#resources1)  
[Úloha 1 - Honzův zkouškový úkol ](#assignment1)  
[Prostředky II - ](#resources2)  
[Úloha 2 - ](#assignment2)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Už jste setkali s nefunční aplikací či chybou v ní? Od toho, aby se to stávalo co nejméně, provádíme testování.
Aplikace, resp. její funkčnost se testuje v několika fázích na několika úrovních. V této lekci se budeme věnovat té nejnižší. Budeme zjišťovat, zda se daný algoritmus chová, jak očekáváme, případně jak by měl.
## Prostředky I - <a name="resources1"/>
V této lekci budete potřebovat papír a tužku, tablet nebo obyčejný notepad a samozřejmě svou ostrou mysl. Zvolte si to, s čím se vám bude nejlépe pracovat.
## Úloha 1 - Honzův zkouškový úkol <a name="assignment1"/>
### Zadání
Student Honza se zúčastnil zkoušky a měl za úkol splnit následující zadání.
1. Vytvořte parametrickou funkci na výpočet faktoriálu.
2. Výsledek pro čísla v rozmezí 0-7 včetně postupně zobrazte na segmentový displej. Pro opakování použijte while cyklus.
3. Je-li výsledek dělitelný 3, rozsviťte libovolnou diodu. Nechejte krátce svítit a poté ji zhasněte.

Honza ale nechodil na přednášky. A tak tam má spoustu chyb. Vaším úkolem je chyby najít.
Postupujte postupně:
1. Kód zanalyzujte a pokuste se najít co nejvíce chyb. Nalezené či domnělé chyby si zapište.
2. Kód přepište do editoru a opravte v něm nalezené chyby.
3. Kód spusťte a ověřte si, jak se vám podařilo chyby odhalit.
4. Kód se pokuste opravit.
### Co budete potřebovat
V této úloze budete potřebovat papír a tužku.
### Co se naučíte
TODO
### Honzova implementace
```python
from microbit import * 

def factorial(number: int) -> int:
    if number < 0:
        return -1
    if number == 0:
        return 1

    factorial_result = 0
    for i in range(number):
        factorial_result += i

    return factorial_result

number = 0

while number < 7:
    fact = factorial(0, 7)
    //TODO: zobraz vysledek
if fact % 3 != 0:
    //TODO: rozsvit diodu
```

### Popis řešení
Honza se dopustil následujících chyb:
1. neví, že faktoriál je součin
    a. `factorial_result` měl iniciálně nastavit na 1
    b. `i` neměl k `factorial_result` přičítat, ale měl jím násobit
2. z výpočtu vynechal číslo 7, protože nerovnost je ostrá
3. funkci faktoriál vytvořil jednoparamaterovou, ale parametry předává dva
4. podmínka má být součástí cyklu, úkolem bylo kontrolu provést pro každé číslo number
5. číslo number zapomněl inkrementovat a vytvořil tak nekonečný cyklus

Honza si zkoušku bude muset zopakovat Správné řešení může vypadat takto:
```python
from microbit import * 

def factorial(number: int) -> int:
    if number < 0:
        return -1
    if number == 0:
        return 1

    factorial_result = 1
    for i in range(1, number + 1):
        factorial_result *= i

    return factorial_result

number = 0

while number < 7:
    fact = factorial(number)
    //TODO: zobraz vysledek
if fact % 3 != 0:
    //TODO: rozsvit diodu
```
### Doplňující poznámky 
TODO
## Prostředky II -  <a name="resources2"/>
TODO
## Úloha 2 - <a name="assignment2"/>
### Zadání
Naimportovat si funkci a otestovat si ručně chování na několika vhodně zvolených vstupech.
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

