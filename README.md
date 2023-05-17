# Lekce 9
#### Testování

## Obsah
[Motivace](#motivace)  
[Prostředky - Testování](#resources1)  
[Úloha 1 - Honzův zkouškový úkol ](#assignment1)  
[Úloha 2 - ](#assignment2)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Už jste setkali s nefunční aplikací či chybou v ní? Od toho, aby se to stávalo co nejméně, provádíme testování. Aplikace, resp. její funkčnost se testuje v několika fázích na několika úrovních. V této lekci se budeme věnovat té nejnižší. Budeme zjišťovat, zda se daný algoritmus chová, jak očekáváme, případně jak by měl. 
## Prostředky - Testování <a name="resources1"/>
Testování je proces, který slouží k ověření správnosti a funkcionality vašeho kódu. Cílem testování je identifikovat chyby, nekonzistence nebo neočekávané chování programu a zajistit, že váš kód pracuje podle očekávání. Testování umožňuje ověřit, zda software pracuje podle specifikací a požadavků.

Při testování je důležité vytvořit testovací scénáře, které obsahují konkrétní kroky, vstupy a očekávané výstupy. Testování může být prováděno manuálně, kdy tester ručně provádí testovací scénáře, nebo automatizovaně, kdy jsou testy spouštěny pomocí automatizovaných skriptů. Správné testování přináší několik výhod, jako je zvýšení kvality softwaru, snížení rizika chyb a problémů v produkci, zajištění spolehlivosti a stabilnosti aplikace a zvýšení uživatelské spokojenosti.

Program lze testovat postupným spouštěním, zakomentováním a odkomentováním kódu. Tento přístup umožňuje postupovat krok za krokem a sledovat, jak se chování programu mění při různých úpravách. Proces identifikace, analýzy a odstraňování chyb v programu se často nazývá debugování či debugging.

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
Žáci se naučí systematicky zkoumat a analyzovat výstupy programu a chápat vztahy mezi jednotlivými částmi kódu. 
### Jak na to
Dejte žákům k dispozici nachystaný kód - ideálně vytištěný na papíru, aby si k němu mohli psát poznámky a koemntovat ho. Dále postupujte dle bodů ze zadání. První krok - analyzování programu vede žáky k práci s cizím kódem a soustředění se na algoritmus krok po kroku. Během přepisování kódu mohou žáci objevit další chyby nebo nepřesnosti a zároveň je hned opravit. Nyní už pracují s jejich vlastním kódem. Následně žáci spouští program a sledují jeho výstup. Mohou si všimnout, jak se program chová a jaké informace zobrazuje. 

Pokud se program nechová dle očekávání, nechte žáky zakomentovat určité části kódu a znovu spustit program, aby viděly, jak tyto změny ovlivňují chování programu. Tímto způsobem začnou chápat, jak jednotlivé části kódu ovlivňují chování programu a jistě se jim ho podaří opravit.

### Honzova implementace
```python
from microbit import * 

def fibonnaci_nth_number(number: int) -> int:
    i_1 = 0
    i_2 = 1
    result = 0
    i = 2
    if number == 2:
        result = 1
    while i < number:
        result = i_1 + i_2
        i_1 = i_2
        i_2 = result
        i += 1
    return result

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
    //TODO: zobraz vysledek na segmentovy displej
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
    //TODO: zobraz vysledek na segmentovy displej
if fact % 3 != 0:
    //TODO: rozsvit diodu
```
### Doplňující poznámky 
TODO
## Úloha 2 - <a name="assignment2"/>
### Zadání
TODO
### Co budete potřebovat
TODO
### Co se naučíte
TODO
### Vzorová implementace
```python
from microbit import *
from motor import *
from trimpot import *

motor = MOTOR(1)
trimpot = TRIMPOT(J1)

fan_setting()

def fan_setting():
    while button_a.is_pressed():
        #vypocet hodnoty speed je korektni
        speed = int((trimpot.get_trimpot_value()/1023)*100)
        motor.set_motor(sped)
    motor.stop()
```
### Popis řešení
TODO
### Doplňující poznámky 
TODO
## Shrnutí <a name="conclusion"/>
- K čemu je testování?
- Jak se jinak říká testování?
- Jaké jsou dva druhy testování?
## Poznámky pro učitele <a name="pozn"/>
TODO

