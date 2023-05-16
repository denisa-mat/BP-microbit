# Lekce 8
### Funkce a metody
## Obsah
[Motivace](#motivace)  
[Prostředky I - ](#resources1)  
[Úloha 1 - ](#assignment1)  
[Prostředky II - ](#resources2)  
[Úloha 2 - ](#assignment2)  
[Úloha 3 - ](#assignment3)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Všimli jste si, že s vám kód opakuje? Ano? Pak vězte, že tomu lze zabránit. Jedno z programátorských (ale i obecně využitlených) pravidel je pravidlo zkráceně pojmenované DRY. DRY je zkratka anglického Don't Repeat Yourself, česky neopakuj se.
Údržba kódu: Když je funkcionalita implementována na více místech ve vašem kódu, je třeba provádět změny na každém místě, kde se nachází. To zvyšuje riziko chyb a ztěžuje údržbu. S dodržováním "dry" principu se zabrání duplikaci kódu a v případě změny je potřeba upravit pouze jedno místo.

Proč dodržovat DRY?
1. Údržba kódu: Když je funkcionalita implementována na více místech ve vašem kódu, je třeba provádět změny na každém místě, kde se nachází. To zvyšuje riziko chyb a ztěžuje údržbu. S dodržováním "dry" principu se zabrání duplikaci kódu a v případě změny je potřeba upravit pouze jedno místo.

1. Čitelnost a porozumitelnost: Duplikovaný kód může ztížit čtení a pochopení programu. Čím méně duplikovaného kódu máte, tím snazší je jeho čtení a porozumění ostatním vývojářům, kteří s ním pracují.

2. Šetření času: Duplikace kódu znamená, že musíte napsat, testovat a udržovat více řádků kódu. Dodržování "dry" principu vám umožní efektivněji využívat svůj čas a zkrátit dobu potřebnou k vývoji a údržbě kódu.

3. Snížení chyb: Duplikovaný kód zvyšuje riziko chyb, protože změny provedené na jednom místě nemusí být provedeny na všech místech, kde se kód duplikuje. Tím se zvyšuje pravděpodobnost, že budou existovat rozdíly mezi různými verzemi kódu, což může vést k neočekávanému chování programu.

4. Refaktorování a znovupoužitelnost: Dodržování "dry" principu umožňuje snadnější refaktorování kódu a zvyšuje jeho znovupoužitelnost. Když je funkcionalita oddělena a sdílena pomocí metod, funkcí nebo tříd, je snazší ji upravit, rozšířit a znovu použít v jiných částech programu.

Celkově lze říci, že dodržování "dry" principu zvyšuje kvalitu a údržbu kódu, usnadňuje spolupráci vývojářů a šetří čas a náklady při vývoji softwaru.

Nejde jen o DRY. Také jste si mohli všimnout, že je kód dlouhý a hůře čitelný. Když však nějakou menší logickou část uzavřete do funkce a funkci si napřílušném místě zavoláte, čtení kódu se stane příjemnějším.

A právě zde nám budou funkce užitečné.

## Prostředky I - <a name="resources1"/>
Existují funkce a procedury. Při vytváření funkcí a procedur, potažmo metod, využíváme stejné klíčové slovo 'def'. Tělo funkce se odsazuje podobně jako u cyklů nebo podmínek. Klíčové slovo 'pass' říká, že tělo funkce/procedury (ale i podmínek nebo cyklů) je prázdné. Tělo je povinné a nelze vynechat, proto využíváme klíčového slova 'pass'.
```python
def moje_rocedura():
    pass
```
V případě funkcí ještě navíc využijeme klíčové slovo return pro vrácení hodnoty.
```python
def multiply():
    product = 2 * 4
    return product
```
Co když ale takovou funkci chceme využít i pro jiná čísla? Pak jsou tu takzvané parametry. Parametry už znáte z hodin matematiky nebo fyziky. Matematickým funckím, jako např. sinus, také předáváme parametry. Pak nám funkce nevrací vždy konstantní hodnotu. Její výstup je závislý na parametrech. Vlastnosti algoritmů platí i pro funkce. Ona funkce je alogritmus. Mějme funkci 'mulitply', bude mít dva parametry. Tyto parametry vynásobí a výsledek nám vrátí.
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
Silně doporučuji využívat tzv. type hinting. Je sice nepovinný, ale přináší mnoho výhod. Některá IDE vám zobrazí deklaraci, kde uvidíte i datové typy parametrů a výstupu. To vám může napovědět co očekávat, sniží to míru chybovosti a pádu programu. Zajdeme-li ještě dál, bude vást to při vytváření funkcí nutit vracet hodnotu stejného typu, dokonce vás to pobízí k vracení logicky stejných hodnot. Výpočet se pro různé parametry může lišit, ale výsledek by měl být logicky stejný.
```python
def multiply(number1: int, number2: int) -> int:
    return number1 * number2
```
Takto vzniklou funci bychom mohli chtít i využít. K tomu využijeme stanoveného identifikátoru funkce, za který přidáme závorky a do závorek paramtery oddělené čárkou.
```python
mulitply(2, 3)

number_a = 2
number_b = 3
mulitply(number_a, number_b)
```

### Procedura
Procedura je ucelený blok kódu, který má svůj identifikátor. Taková procedura vždy jen něco provádí, mění hodnoty v proměnných, upravuje soubory atd. Nic nevrací.

### Funkce
Funkce je také ucelený blok kódu a též má vlastní identifikátor. Funkce nic nemění, pouze vypočítá/zjistí a vrací nějakou hodnotu. Vrácená hodnota je vždy jen jedna. Potřebujeme-li jich vracet více, využijeme nějakou vhodnou datovou strukturu, např. pole.

### Metoda
Metoda není nic jiného než procedura nebo funkce. Rozdíl je však v tom, jaké využíváme paradigma. Imperativní, kterému jsme se věnovali doposud, využívá procedury a funkce. S metodami se setkáme v objektově orientovaném programování (OOP).
Už je ale znáte, setkali jste se s nimi už v první lekci. Na displej microbita jste vypisovali text či zobrazovali nějaký obrazec. Objekt 'display', metoda 'scroll'. Objekt 'display' pochází z modulu microbit a ten má metodu 'scroll'. Metody se volají podobně jako funkce. Rozdíl však je v tom, že metoda se volá "přes" tečku. Více v lekci OOP.

```python
from microbit import * 
    display.scroll("Hello World")
```
 

## Úloha 1 - Proměnné <a name="assignment1"/>
### Zadání
Vytvořte proceduru, která rozsvítí diody jako na semaforu. Zvolte vhodné konstanty pro délu svícení diod. Metodu poté zavolejte a opakujte desetkrát. K opakování použijte for cyklus.
### Co budete potřebovat
microbit, diody
### Co se naučíte
Naučíte se tvořit procedury a následně je volat.
### Vzorová implementace
```python
from microbit import * 

def switch_on_traffic_lights() -> None:
    pass

for _ in range(10):
    switch_on_traffic_lights()
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

