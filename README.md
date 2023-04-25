# Lekce 2
### podtitul

### Obsah
[Motivace](#motivace)  
[Prostředky](#resources)  
[Úloha 1](#assignment1)  
[Úloha 2](#assignment2)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  
<<<<<<< HEAD
<a name="motivace"/>
## Motivace
Setkali jste se někde s proměnnými?
	Otázka má žáky navést k matematice a fyzice, kde se s rovnicemi potkají v každé rovnici s neznámou. 
	
Proměnné jsou důležité pro matematické výpočty, například řešení rovnic, vypočítávání průměru, mediánu a dalších matematických funkcí.

Zjevné je také využití proměnných při vývoji her, kde mohou uchovávat informace o hráči, jako jsou jeho životy, skóre nebo stavové informace.

Dalším důležitým aspektem proměnných je, že umožňují programátorům vytvářet opakovaně použitelný kód a snižovat tak duplikaci kódu. Tím se zvyšuje efektivita vývoje a snižují se náklady na vývoj softwaru protože zjednodušují práci programátorům.
<a name="resources"/>
## Prostředky I - teoretická část
...
### Proměnná
Proměnná je základní stavební kamen programování a označuje místo v paměti počítače, které je určeno pro ukládání hodnot. Proměnné mají název, datový typ a obsahují konkrétní hodnotu, která může být v průběhu programu měněna. Používají se pro ukládání vstupních dat, mezivýsledků a výstupních dat programu. Díky proměnným mohou programy uchovávat informace a provádět s nimi operace, což umožňuje tvorbu dynamických a interaktivních programů.
### Datový typ
Datový typ je termín, který definuje jaké druhy hodnot lze uložit do proměnné. Konkrétně určuje, jaký typ dat může být uložen v paměti. Každý programovací jazyk má své vlastní datové typy, například celá čísla (integer), reálná čísla (float), textové řetězce (string), pole (array) atd. Používání správných datových typů je důležité pro korektní běh programu a tvorbu efektivních a bezpečných aplikací.
<a name="assignment1"/>
## Úloha 1 - Proměnné

=======

## Motivace <a name="motivace"/>
...

## Prostředky - teoretická část <a name="resources"/>
...

## Úloha 1 - <a name="assignment1"/>
>>>>>>> 1799d30187534d210269276d9e207b06b8764a90
### Zadání
Napište program, který bude v nekonečném cyklu počítat Fibonaccioho posloupnosta vypisovat její výpočet na micro:bit (použijte funkci scrool, kterou jste využili v minulé lekci). Program bude obsahovat tři proměnné - dva sčítance a výsledek. Proměnné vhodně pojmenujte. První výpis bude vypadat následovně: 0+1=1
### Co budete potřebovat
K této úloze nejsou potřeba žádné senzory a moduly.
### Co se naučíte
Cílem úlohy je Vyzkoušet si práci s proměnnými a vybranou operací nad datovým typem int. Zároveň si žáci zopakují práci s editorem a micro:bitem z minulé lekce.
### Vzorová implementace
```python
from microbit import * 

number1 = 0
number2 = 1   

while True:   
	# Provedeni souctu a jeho ulozeni do promenne sum
    sum = number1 + number2     
	# Zobrazeni vypoctu a vysledku na microbit
    display.scroll(str(number1) + "+" + str(number2) + "=" + str(sum))
	# Prepsani promenne number1
    number1 = number2
	# Prepsani promenne number2
    number2 = sum
```python

### Popis řešení
Na řádcích 3 a 4 jsou vytvořené proměnné, do kterých jsou uložené výchozí hodnoty Fibobacciho posloupnosti 0 a 1. Zbytek programu je obalený v nekonečném while cyklu. Na řádku 7 je do proměnné sum přiřazen součet dvou předchozích členů posloupnosti, které jsou uložené v proměnných number1 a number2. Metoda scroll zavolaná na objektu display postupně zobrazuje výpočet a výsledek na micro:bitu.

### Doplňující poznámky 
...
<<<<<<< HEAD
<a name="assignment2"/>
## Prostředky II - teoretická část
### NezhaKit

## Úloha 2 - 
=======

## Úloha 2 - <a name="assignment2"/>
>>>>>>> 1799d30187534d210269276d9e207b06b8764a90
### Zadání
### Co budete potřebovat
### Co se naučíte
### Vzorová implementace
### Popis řešení
### Doplňující poznámky 
...

## Shrnutí <a name="conclusion"/>
...

## Poznámky pro učitele <a name="pozn"/>
