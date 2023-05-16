# Lekce 8
#### Funkce a metody
## Obsah
[Motivace](#motivace)  
[Prostředky - Funkce a metody](#resources1)  
[Úloha 1 - Semafor](#assignment1)  
[Úloha 2 - SOS ](#assignment2)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Všimli jste si, že s vám kód opakuje? Ano? Pak vězte, že tomu lze zabránit. Jedno z programátorských (ale i obecně využitlených) pravidel je pravidlo zkráceně pojmenované DRY. DRY je zkratka anglického Don't Repeat Yourself, česky neopakuj sám sebe.
Když potřebujete využít nějakou část kódu na více místech v programu, je v případě úpravy potřeba provádět změny na každém místě, kde se nachází. To zvyšuje riziko chyb a ztěžuje údržbu. S dodržováním "dry" principu se zabrání duplikaci kódu a změny stačí provádět pouze na jednom místě, což šetří čas. Dále, eliminace duplikovaného kódu zvyšuje čitelnost a porozumitelnost programu, což usnadňuje spolupráci mezi vývojáři. Dodržování "dry" principu také umožňuje snadnější refaktorování a znovupoužitelnost kódu v různých částech programu. 

Nejde jen o DRY. Také jste si mohli všimnout, že je kód dlouhý a hůře čitelný. Když však nějakou menší logickou část uzavřete do vhodně pojmenované funkce a tu na přílušném místě zavoláte, čtení kódu se stane příjemnějším.

A právě zde budou funkce užitečné.

## Prostředky - Funkce a metody <a name="resources1"/>
Termín funkce odkazuje na samostatnou část kódu, která provádí určitou úlohu nebo výpočet. Funkce je blok kódu, který může přijímat vstupní hodnoty (argumenty), provádět určité operace a vrátit výsledek (návratovou hodnotu). Funkce slouží k rozdělení programu na menší, logicky oddělené části. 

Při vytváření funkcí potažmo metod, využíváme stejné klíčové slovo `def`. Tělo funkce se odsazuje podobně jako u cyklů nebo podmínek. Klíčové slovo `pass` říká, že tělo funkce/procedury (ale i podmínek nebo cyklů) je prázdné. Tělo je povinné a nelze vynechat, proto využíváme klíčového slova `pass`.
```python
def moje_rocedura():
    pass
```
V případě funkcí ještě navíc využijeme klíčové slovo `return` pro vrácení hodnoty.
```python
def multiply():
    product = 2 * 4
    return product
```
Co když ale takovou funkci chceme využít i pro jiná čísla? Pak jsou tu takzvané parametry. Parametry už znáte z hodin matematiky nebo fyziky. Matematickým funckím, jako např. sinus, také předáváme parametry. Pak nám funkce nevrací vždy konstantní hodnotu. Její výstup je závislý na vstupu - parametrech. Vlastnosti algoritmů platí i pro funkce. Ona funkce je vlastně alogritmus. Mějme funkci `multiply`, která bude mít dva parametry. Tyto parametry funkce vynásobí a výsledek nám vrátí.
```python
def multiply(number1, number2):
    product = number1 * number2
    return product
```
Lze vrátit i výraz. Není tedy nutné hodnotu vypočítat, uložit do proměnné a až poté výsledek vracet.
```python
def multiply(number1, number2):
    return number1 * number2
```
Silně doporučuji využívat tzv. type hinting. Je v Pythonu nepovinný, ale přináší mnoho výhod. Některá IDE vám zobrazí deklaraci, kde uvidíte i datové typy parametrů a výstupu. To vám může napovědět co očekávat, sniží to míru chybovosti a pádu programu. Zajdeme-li ještě dál, bude vás to při vytváření funkcí nutit vracet hodnotu stejného typu, dokonce vás to pobízí k vracení logicky stejných hodnot.
```python
def multiply(number1: int, number2: int) -> int:
    return number1 * number2
```
Když takto vzniklou funkci chceme využít, využijeme její název, za který přidáme závorky a do závorek parametry oddělené čárkou. Tomu říkáme volání funkce.
```python
def multiply(number1: int, number2: int) -> int:
    return number1 * number2

product = mulitply(2, 3)

number_a = 2
number_b = 3
#funkci je možné předat hodnoty i prostřednictím proměnných
product = mulitply(number_a, number_b)
```

### Funkce
Funkce je ucelený blok kódu s vlastním identifikátorem. Funkce něco provede a vrátí nějakou hodnotu, pokud nepotřebujeme, aby funkce něco vrátila vrátíme None. Vrácená hodnota je vždy jen jedna. Potřebujeme-li jich vracet více, využijeme nějakou vhodnou datovou strukturu, např. `list` nebo `touple`.

### Metoda
Metoda není nic jiného než funkce. Rozdíl je však v tom, jaké využíváme paradigma. Imperativní, kterému jsme se věnovali doposud, využívá funkce. S metodami se setkáme v objektově orientovaném programování (OOP).
Už je ale znáte, setkali jste se s nimi již v první lekci. Na displej micro:bita jste vypisovali text či zobrazovali nějaký obrazec. Objekt `display`, metoda `scroll`. Objekt `display` pochází z modulu microbit a ten má metodu `scroll`. Metody se volají podobně jako funkce. Rozdíl však je v tom, že metoda se volá "přes" tečku. Více v lekci OOP.

```python
from microbit import * 
    display.scroll("Hello World")
```
 
## Úloha 1 - Semafor <a name="assignment1"/>
### Zadání
Vytvořte funkci, která rozsvítí diody jako na semaforu. Zvolte vhodnou délku svícení diod. Metodu poté zavolejte a opakujte desetkrát. K opakování použijte for cyklus.
### Co budete potřebovat
K řešení úlohy využijete všechny tři LED diody, které jsou součástí Nezha sady.
### Co se naučíte
Žáci se naučí vytvářet vlastní funkce a ve vhodnou chvíli je zavolat.
### Jak postupovat
Nejprve naimportujte potřebný modul led a následně vytvořte objekty reprezentující tři 

### Vzorová implementace
```python
from microbit import * 
from led import *

red_diod = LED(J1)
yellow_diod = LED(J2)
green_diod = LED(J3)

def switch_on_traffic_lights() -> None:
    sleep_time = 2000

    red_diod.turn_led_on()
    sleep(sleep_time)
    red_diod.turn_led_off()
    yellow_diod.turn_led_on()
    sleep(sleep_time/2)
    yellow_diod.turn_led_off()
    green_diod.turn_led_on()
    sleep(sleep_time)
    green_diod.turn_led_off()
    yellow_diod.turn_led_on()
    sleep(sleep_time/2)
    yellow_diod.turn_led_off()

for _ in range(10):
    switch_on_traffic_lights()
```
### Popis řešení
Nejprve je naimportován potřebný modul led a následně vytvořeny objekty diod. Na řádku osm je hlavička funkce `switch_on_traffic_lights()`, která nebere žádné parametry a vidíme, že vrací `None`. Následuje tělo funkce, které začáná vytvořením proměnné `sleep_time` udržující hodnotu délky svícení jedné barvy semaforu. Dále jsou jen rozsvěceny a zhasínány led diody v daném časovém intervalu. Již mimo funkci, vhlavním toku programu je cyklus for, který zajistí deset zavolámí výše vytvořené funkce `switch_on_traffic_lights()`.
### Doplňující poznámky 
Možná žáky napadne dále funkci rozdělit na menší funkce, pokud objeví opakující se vzor, který by stálo za to dát do funkce, nechte je to udělat.

## Úloha 2 - SOS <a name="assignment2"/>
### Zadání
Napište funkci, která bude blikat SOS v Morseově abecedě. Nezapomeňte, že uvnitř funkce můžete volat jiné funkce. Nejprve napište funkci pro jeden znak, která bude brát jako parametr délku jednoho znaku v milisekundách. Dále vytvořte funkce pro obě potřebná písmena a teprve potom pro celý signál SOS.
### Co budete potřebovat
Pro tuto úlohu bude z modulů stačit jedna led dioda z Nezha sady.
### Co se naučíte
V úloze si žáci vyzkouší vytvořit funkci s parametrem a několik dalších malých funkcí, které budou volány uvnitř jiných funkcí, zároveň je součástí této úlohy metoda code review.
### Jak postupovat
Funkce jsou malé a jak mají vypadat je popsané v zadání, můžete tedy zkusit dát ákům zadání a nechat je pracovat individuálně (případně ve dvojicích. Nejprve je je vytvořena funkce `dot_or_dash(pause_time)`, parametr pause time je číselná hodnota udávající, jak dlouho bude led svítit dle tohoto se jedná o čárku nebo tečku. Dále následují funkce pro zablikání písmene S a písmene O. Oba tyto znaky se skládají ze tří signálů, které jsou por O dlouhé a pro S krátké. Poslední funkce rozbliká celý kód SOS a to pomocí zavolání jendotlivých písmen. 
### Vzorová implementace
```python
from microbit import * 
from led import *

def dot_or_dash(int: pause_time) -> None:
    led_diod.turn_led_on()
    sleep(pause_time)
    led_diod.turn_led_off()

def morse_S() -> None:
    for _ in range(3):
        dot_or_dash(200)

def morse_O() -> None:
    for _ in range(3):
        dot_or_dash(500)

def morse_SOS() -> None:
    morse_S()
    sleep(800)
    morse_O()
    sleep(800)
    morse_S()
```
### Popis řešení
Řešení se skládá ze čtyř funkcí. První `dot_or_dash()`bere jako parametr délku svícení diody. Funkce morse_S a morse_O pomocí for cyklu třikrát zablikají. Ve funkci SOS, jsou využity předchozí vytvořené funkce a funkce `sleep()` pro znázornění ukončení písmene.

### Doplňující poznámky 
Vzorová implementace by se jistě dala ještě vylepšit například využitím konstatních globálních proměnných, v nichž by byli uloženy hodnoty pro dobu čekání. 

## Shrnutí <a name="conclusion"/>
- Co je to funkce?
- Jaký je rozdíl mezi funkcí a metodou?
- Kolik parametrů může brát funkce?

## Poznámky pro učitele <a name="pozn"/>
Pro zjednodušení je zde vynechán pojem procedura. Procedury jsou zahrnuty pod pojem funkce. Procedura je ucelený blok kódu, který má svůj identifikátor a na rozdíl od funkce jen něco provádí, například mění hodnoty v proměnných, upravuje soubory. Její návratový typ je vždy `None`.

