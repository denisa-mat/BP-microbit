# Lekce 2
### proměnné, datové typy, Nezha sada

## Obsah
[Motivace](#motivace)  
[Prostředky I - Proměnné, datové typy](#resources1)  
[Úloha 1 - Proměnné](#assignment1)  
[Prostředky II - Nezha kit](#resources2)  
[Úloha 2 - Seznámení s Nezha kitem](#assignment2)  
[Úloha 3](#assignment3)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Setkali jste se někde s proměnnými?
Otázka má žáky navést k matematice a fyzice, kde se s proměnnými potkají v každé rovnici s neznámou. 

Proměnné jsou důležité pro matematické výpočty, například řešení rovnic, výpočet průměru, mediánu a dalších matematických funkcí. Zjevné je také využití proměnných při vývoji her, kde mohou uchovávat informace o hráči, jako jsou jeho životy, skóre nebo stavové informace.

Dalším důležitým aspektem proměnných je, že umožňují programátorům vytvářet opakovaně použitelný kód a snižovat tak duplikaci kódu. Tím se zvyšuje efektivita vývoje a snižují se náklady na vývoj softwaru, protože zjednodušují práci programátorům.

## Prostředky I - Proměnné, datové typy <a name="resources1"/>
### Proměnná
Proměnná je základní stavební kamen programování a označuje místo v paměti počítače, které je určeno pro ukládání hodnot. Proměnné mají název, datový typ a obsahují konkrétní hodnotu, která může být v průběhu programu měněna. Používají se pro ukládání vstupních dat, mezivýsledků a výstupních dat programu. Díky proměnným mohou programy uchovávat informace a provádět s nimi operace, což umožňuje tvorbu dynamických a interaktivních programů.
### Datový typ
Datový typ definuje, jaké druhy hodnot lze uložit do proměnné. Konkrétně určuje, jaký typ dat může být uložen v paměti počítače. Každý programovací jazyk má své vlastní datové typy, například celá čísla (integer), reálná čísla (float), textové řetězce (string), pole (array). Používání správných datových typů je důležité pro korektní běh programu a tvorbu efektivních a bezpečných aplikací.
### Operace s proměnnými
S proměnnými lze provádět několik základních operací. Ne všechny operace lze provádět nad všemi datovými typy. Nad číselnými proměnnými můžeme provádět matematické operace s klasickým způsobem (sčítání značíme +, odčítání -, násobení **, dělení /). Operaci + lze použít také na typ string, kde funguje jako řetězení. Protože Python není typovaný jazyk, je na programátorovi, aby věděl, jaký datový typ je v proměnné uložený. Python při přiřazení nové hodnoty umožňuje vložit hodnotu jiného datového typu. V případě, že se pokusíme provést operaci, která na dané kombinaci typů není podporována editor nás upozorní červenou značkou před číslem řádku a chybovou zprávou.

<p align="center">
  <img src=/img/spatneTypy.png alt="Operace na nepodporované kombinaci typů width="100%">
  <em>Operace na nepodporované kombinaci typů</em>
</p>

## Úloha 1 - Proměnné <a name="assignment1"/>
### Zadání
Napište program, který bude v nekonečném cyklu počítat Fibonaccioho posloupnost a vypisovat její výpočet na micro:bit (použijte funkci scroll, kterou jste využili v minulé lekci). Program bude obsahovat tři proměnné – dva sčítance a výsledek. Proměnné vhodně pojmenujte. První výpis bude vypadat následovně: 0+1=1
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
Na řádcích 3 a 4 jsou vytvořené proměnné, do kterých jsou uložené výchozí hodnoty Fibonacciho posloupnosti 0 a 1. Zbytek programu je obalený v nekonečném while cyklu. Na řádku 7 je do proměnné sum přiřazen součet dvou předchozích členů posloupnosti, které jsou uložené v proměnných number1 a number2. 

Metoda scroll zavolaná na objektu display postupně zobrazuje výpočet a výsledek na micro:bit. Protože scroll bere pouze argumenty typu string přetypujte proměnné number1 a number2 pomocí funkce str(). Aplikace operace + na hodnoty typu string funguje jako řetězení (konkatenace).
Na řádku 9 je do proměnné number1 uložena hodnota proměnné number2, na řádku 10 je do proměnné number2 uložena hodnota z proměnné sum. Tato změna hodnot v proměnných umožňuje v další iteraci vypočítat následující hodnotu Fibonacciho posloupnosti.

### Doplňující poznámky 
Fibonacciho posloupnost je posloupnost čísel začínající nulou a jedničkou, kde každé následující číslo je součet předchozích dvou. Fibonacciho posloupnost se vyskytuje v řadě různých oblastí od přírodních věd až po design a umění.

## Prostředky II - Nezha kit <a name="resources2"/>
### NezhaKit
Nezha Inventors Kit je robotická stavebnice navržená pro micro:bit a je kompatibilní s první i druhou verzí. Tato sada pro vynálezce obsahuje několik senzorů PlanetX, díky nimž je možné se sadou vytvořit desítky různých projektů. Základ setu tvoří modul pro umístění micro:bitu.

Pro propojení jednotlivých modulů jsou použity vodiče s konektory RJ11. Stačí zacvaknout a senzory jsou propojené s modulem a tedy i s micro:bitem. Propojení je snadné a spolehlivé. Další výhodou je kompatibilita Nezha kitu se stavebnicí lego a Fischertechnik. Sada je uložena v praktickém boxu, který obsahuje:
- Nezha rozšiřující modul pro micro:bit (zabudovaný akumulátor LiPol 900 mAh, porty pro senzory a další moduly, konektory pro serva a motory, konektor pro micro:bit)
- 8 elektronických modulů (3 x LED modul, potenciometr, snímač vlhkosti, snímač vzdálenosti, snímač nárazu, snímač čáry)
- 2 x DC motor pro realizaci otáčivých pohybů
- servo 360 ° pro natočení na přesný úhel v rozsahu 0 - 360 °
- propojovací vodiče s konektory RJ11, USB kabel pro nahrání programu do micro:bitu
- kola s pneumatikami pro LEGO®, rejdovací kolečko pro jezdícího robota
- více než 400 součástí kompatibilních s LEGO® Technic
- mapa s čárou pro ježdění po čáře

<p align="center">
  <img src=/img/nezhaKit.jpg alt="Obsah Nezha kitu" width="100%">
  <em>Obsah Nezha kitu</em>
</p>

Do modulu Nezha připojíme micro:bit pomocí hranového konektoru. Senzory následně připojíme k modulu dle barev pomocí příslušných kabelů a konektorů, dle následujícího schématu.

<p align="center">
  <img src=/img/nezhaSchema.png alt="Schéma Nezha kitu" width="100%">
  <em>Schéma Nezha kitu</em>
</p>

## Úloha 2 - Seznámení s Nezha kitem <a name="assignment2"/>
### Zadání
Druhou úlohou bude použít již vytvořený program a rozsvítit na PlanetX LED matrix modulu postupně počet diod dle Fibonacciho posloupnosti. Až počet přesáhne zadaný počet budou svítit všechny diody.
### Co budete potřebovat
Pro tuto úlohu bude potřeba modul Nezha a PlanetX LED matrix modul
### Co se naučíte
Cílem této úlohy je vyzkoušet použití rozšiřujícího Nezha modulu jednoho z dalších modulů.
### Vzorová implementace
```python
from microbit import *
from matrix import *
from nezha import *

nezha = NEZHA()
matrix = MATRIX()

number1 = 0
number2 = 1
sum = number1 + number2

while sum <= 16*8:
    print(sum)
    matrix.set_matrix_draw_position(sum)
    number1 = number2
    number2 = sum
    sum = number1 + number2
    sleep(500)
```

### Popis řešení
TODO
### Doplňující poznámky 
TODO
## Úloha 3 - Proměnné a měření vzdálenosti <a name="assignment3"/>
### Zadání
TODO
### Co budete potřebovat
TODO
### Co se naučíte
TODO
### Vzorová implementace
TODO
### Popis řešení
TODO
### Doplňující poznámky 
TODO
## Shrnutí <a name="conclusion"/>
TODO
## Poznámky pro učitele <a name="pozn"/>
TODO
