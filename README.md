# Lekce 9
#### Testování

## Obsah
[Motivace](#motivace)  
[Prostředky - Testování](#resources1)  
[Úloha 1 - Honzův zkouškový úkol ](#assignment1)  
[Úloha 2 - Větrák](#assignment2)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Už jste setkali s nefunční aplikací či chybou v ní? Od toho, aby se to stávalo co nejméně, provádíme testování. Aplikace, resp. její funkčnost se testuje v několika fázích na několika úrovních. V této lekci se budeme věnovat té nejnižší. Budeme zjišťovat, zda se daný algoritmus chová, jak očekáváme, případně jak by měl. 
## Prostředky – Testování <a name="resources1"/>
Testování je proces, který slouží k ověření správnosti a funkcionality vašeho kódu. Cílem testování je identifikovat chyby, nekonzistence nebo neočekávané chování programu a zajistit, že váš kód pracuje podle očekávání. Testování umožňuje ověřit, zda software pracuje podle specifikací a požadavků.

Při testování je důležité vytvořit testovací scénáře, které obsahují konkrétní kroky, vstupy a očekávané výstupy. Testování může být prováděno manuálně, kdy tester ručně provádí testovací scénáře, nebo automatizovaně, kdy jsou testy spouštěny pomocí automatizovaných skriptů. Správné testování přináší několik výhod, jako je zvýšení kvality softwaru, snížení rizika chyb a problémů v produkci, zajištění spolehlivosti a stabilnosti aplikace a zvýšení uživatelské spokojenosti.

Program lze testovat postupným spouštěním, zakomentováním a odkomentováním kódu. Tento přístup umožňuje postupovat krok za krokem a sledovat, jak se chování programu mění při různých úpravách. Proces identifikace, analýzy a odstraňování chyb v programu se často nazývá debuggování či debugging.

## Úloha 1 - Honzův zkouškový úkol <a name="assignment1"/>
### Zadání
Student Honza se zúčastnil zkoušky a měl za úkol splnit následující zadání.
1. Vytvořte parametrickou funkci na výpočet faktoriálu.
2. Výsledek pro čísla v rozmezí 0-7 včetně postupně zobrazte na segmentový displej. Pro opakování použijte while cyklus.

Honza ale nechodil na přednášky. A tak tam má spoustu chyb. Vaším úkolem je chyby najít.
Postupujte postupně:
1. Kód zanalyzujte a pokuste se najít co nejvíce chyb. Nalezené či domnělé chyby si zapište.
2. Kód přepište do editoru a opravte v něm nalezené chyby.
3. Kód spusťte a ověřte si, jak se vám podařilo chyby odhalit.
4. Kód se pokuste opravit.
### Co budete potřebovat
V této úloze se hodí mít papír a tužku. Dále je potřeba segmentový diplej – nixietube, který není součástí sady.
### Co se naučíte
Žáci se naučí systematicky zkoumat a analyzovat výstupy programu a chápat vztahy mezi jednotlivými částmi kódu. 
### Jak na to
Rozdělte žáky do skupin a dejte jim k dispozici nachystaný kód – ideálně vytištěný na papíru, aby si k němu mohli psát poznámky a komentovat ho. Dále postupujte dle bodů ze zadání. První krok – analyzování programu vede žáky k práci s cizím kódem a soustředění se na algoritmus krok po kroku. Během přepisování kódu mohou žáci objevit další chyby nebo nepřesnosti a zároveň je hned opravit. Nyní už pracují s jejich vlastním kódem. Následně žáci spouští program a sledují jeho výstup. Mohou si všimnout, jak se program chová a jaké informace zobrazuje. 

Pokud se program nechová dle očekávání, nechte žáky zakomentovat určité části kódu a znovu spustit program, aby viděly, jak tyto změny ovlivňují chování programu. Tímto způsobem začnou chápat, jak jednotlivé části kódu ovlivňují chování programu a jistě se jim ho podaří opravit.

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
        factorial_result * i

    return factorial_result

number = 0

while number < 7:
    fact = factorial(0, 7)
    #TODO: zobraz vysledek na segmentovy displej
```

### Popis řešení
Honza se dopustil následujících chyb:
1. při výpočtu faktoriálu nikam neukládá výsledek operace (zahazuje ho)
2. z výpočtu vynechal číslo 7, protože nerovnost je ostrá (faktoriál sedmi se na displej ještě vejde)
3. funkci faktoriál vytvořil jednoparamaterovou, ale při volání parametry předává dva
5. číslo `number` zapomněl inkrementovat a vytvořil tak nekonečný cyklus

Honza si zkoušku bude muset zopakovat. Správné řešení může vypadat takto:
```python
from microbit import * 
from nixietube import *
from led import *

nixietube_display = NIXIETUBE(J1)

def factorial(number: int) -> int:
    if number < 0:
        return -1
    elif number == 0:
        return 1

    factorial_result = 1

    for i in range(1, number + 1):
        factorial_result = factorial_result * i

    return factorial_result

number = 0

while number < 8:
    fact = factorial(number)
    nixietube_display.set_show_num(fact)
    sleep(2000)
    number += 1
```
### Doplňující poznámky 
Pokud žáci neznají faktoriál, nechte je si to vyhledat a případně se i podívat, jak ho lze implementovat. Stále však dbejte na to, aby opravili zadaný kód. Mohlo by je to svádět k napsání nového programu, což není cílem této úlohy.
## Úloha 2 - Větrák <a name="assignment2"/>
### Zadání
Sestavte si větráček, poháněný motorem. Rychlost motoru bude ovládaná pomocí potenciometru (trimpot). Následně se pokuste opravit kód níže a zprovoznit větrák.
### Co budete potřebovat
V této úloze budete pracovat s jedním motorem a potenciometrem, obojí je součástí Nezha sady.
### Co se naučíte
Žáci si upevní schopnost číst a opravit cizí kód.
### Jak postupovat
Podobně jako v předchozí úloze nechte žáky opravit zadaný kód. Úloha Tato úloha je jednodušší a po zvládnutí předchozí by s ní žáci neměli mít problém. Součástí je sestavení větráku, například dle obrázku níže.

### Implementace k opravení
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
První chyba v kódu je volání funkce `fan_setting()`. Funkci lze v Pythonu volat až po jejím vytvoření. Dále je chyba v podmínce while cyklu – chybí `not`, pokud bychom podmínku nechali jak je, tělo cyklu by se vykonalo jen pokud po zavolání funkce bylo tlačítko `A` stisknuto. Na řádku 14 je chybně napsaná proměnná `speed` jako `sped`, což v aktuálním kontextu neexistuje. Poslední chyba je při zastavení motoru, metoda stop neexistuje, je potřeba zavolat metodu `set_motor_stop`.

```python
from microbit import *
from motor import *
from trimpot import *

motor = MOTOR(1)
trimpot = TRIMPOT(J1)

def fan_setting():
    while not button_a.is_pressed():
        #vypocet hodnoty speed je korektni
        speed = int((trimpot.get_trimpot_value()/1023)*100)
        motor.set_motor(speed)
    motor.set_motor_stop()

fan_setting()
```

### Doplňující poznámky 
Hodnotu, kterou vrací metoda `get_trimpot_value` je třeba přepočítat, protože metoda `set_motor()` je schopná zpracovat pouze hodnoty <-100, 100>, ale bez přepočítání by maximální hodnota byla v intervalu <0, 1023>
## Shrnutí <a name="conclusion"/>
- K čemu je testování?
- Jak se jinak říká testování?
- Jaké jsou dva druhy testování?
## Poznámky pro učitele <a name="pozn"/>
Pokus byste se chtěli pustit do automatizovaného testování, základní informace v češtině můžete získat například na webu [naucse.python.cz](https://naucse.python.cz/course/pyladies/beginners/testing/).

