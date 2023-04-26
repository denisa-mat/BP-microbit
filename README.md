# Lekce 2
### podtitul

### Obsah
[Motivace](#motivace)  
[Prostředky](#resources1)  
[Úloha 1](#assignment1)  
[Prostředky](#resources2)  
[Úloha 2](#assignment2)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Setkali jste se někde s proměnnými?
Otázka má žáky navést k matematice a fyzice, kde se s proměnnými potkají v každé rovnici s neznámou. 
	
Proměnné jsou důležité pro matematické výpočty, například řešení rovnic, výpočet průměru, mediánu a dalších matematických funkcí. Zjevné je také využití proměnných při vývoji her, kde mohou uchovávat informace o hráči, jako jsou jeho životy, skóre nebo stavové informace.

Dalším důležitým aspektem proměnných je, že umožňují programátorům vytvářet opakovaně použitelný kód a snižovat tak duplikaci kódu. Tím se zvyšuje efektivita vývoje a snižují se náklady na vývoj softwaru protože zjednodušují práci programátorům.

## Prostředky I - teoretická část <a name="resources1"/>
### Proměnná
Proměnná je základní stavební kamen programování a označuje místo v paměti počítače, které je určeno pro ukládání hodnot. Proměnné mají název, datový typ a obsahují konkrétní hodnotu, která může být v průběhu programu měněna. Používají se pro ukládání vstupních dat, mezivýsledků a výstupních dat programu. Díky proměnným mohou programy uchovávat informace a provádět s nimi operace, což umožňuje tvorbu dynamických a interaktivních programů.
### Datový typ
Datový typ definuje, jaké druhy hodnot lze uložit do proměnné. Konkrétně určuje, jaký typ dat může být uložen v paměti počítače. Každý programovací jazyk má své vlastní datové typy, například celá čísla (integer), reálná čísla (float), textové řetězce (string), pole (array). Používání správných datových typů je důležité pro korektní běh programu a tvorbu efektivních a bezpečných aplikací.
### Operace s proměnnými
S proměnnými lze provádět několik základních operací. Ne všechny operace lze provádět nad všemi datovými typy. Nad číselnými proměnnými můžeme provádět matematické operace s klasickým způsobem (sčítání značíme +, odčítání -, násobení **, dělení /). Operaci + lze použít také na typ string, kde funguje jako řetězení. Protože Python není typovaný jazyk, je na programátorovi, aby věděl jaký datový typ je v proměnné uložený. Python při přiřazení nové hodnoty umožňuje vložit hodnotu jiného datového typu. V případě, že se pokusíme provést operaci, která na dané kombinaci typů není podporována editor nás upozorní červenou značkou před číslem řádku a chybovou zprávou.

![Semantic description of image](/img/spatneTypy.png "Operace na nepodporovanou kombinací typů")*Operace na nepodporovanou kombinací typů*

## Úloha 1 - Proměnné <a name="assignment1"/>
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
    sum = number1 + number2     
    display.scroll(str(number1) + "+" + str(number2) + "=" + str(sum))
    number1 = number2
    number2 = sum
```

### Popis řešení
Na řádcích 3 a 4 jsou vytvořené proměnné, do kterých jsou uložené výchozí hodnoty Fibobacciho posloupnosti 0 a 1. Zbytek programu je obalený v nekonečném while cyklu. Na řádku 7 je do proměnné sum přiřazen součet dvou předchozích členů posloupnosti, které jsou uložené v proměnných number1 a number2. 

Metoda scroll zavolaná na objektu display postupně zobrazuje výpočet a výsledek na micro:bitu. Protože scroll bere pouze argumenty typu string přetypujte proměnné number1 a number2 pomocí funkce str(). Aplikace operace + na hodnoty typu string funguje jako řetězení (konkatenace).
Na řádku 9 je do proměnné number1 uložena hodnota proměnné number2, na řádku 10 je do proměnné number2 uložena hodnota z proměnné sum. Tato změna hodnot v proměnných umožňuje v další iteraci vypočítat následující hodnotu Fibonacciho posloupnosti.

### Doplňující poznámky 
Fibonnaciho posloupnost je posloupnost čísel začínající nulou a jednočkou, kde každé následující číslo je součet předchozích dvou. Fibonacciho posloupnost se vyskytuje v řadě různých oblastí od přírodních věd až po design a umění.

## Prostředky II - teoretická část <a name="resources2"/>

### NezhaKit

![Semantic description of image](/img/nezhaKit.jpg "Obsah Nezha kitu")*Obsah Nezha kitu*

![Semantic description of image](/img/nezhaSchema.png "Schéma Nezha kitu")*Schéma Nezha kitu*

<a name="assignment2"/>
## Úloha 2 - 
...
### Zadání
### Co budete potřebovat
### Co se naučíte
### Vzorová implementace
### Popis řešení
### Doplňující poznámky 
...
<a name="conclusion"/>
## Shrnutí
...
<a name="pozn"/>
## Poznámky pro učitele
...
