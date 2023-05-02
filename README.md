# Lekce 2
### proměnné, datové typy, Nezha sada

## Obsah
[Motivace](#motivace)  
[Prostředky I - Proměnné, datové typy](#resources1)  
[Úloha 1 - Proměnné, Fibonacciho posloupnost ](#assignment1)  
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

Pro přiřazení hodnoty do proměnné v Pythonu použijte operátor přiřazení `=` následovaný hodnotou, kterou chcete uložit do proměnné. Například:

```python
# přiřazení hodnoty 10 do proměnné x
x = 10

# přiřazení řetězce 'ahoj' do proměnné y
y = "ahoj"

# přiřazení logické hodnoty True do proměnné z
z = True
```
Při pojemnování proměnných v Pythonu dodržujte následující pravidla:
- Název proměnné může obsahovat pouze písmena (velká nebo malá), číslice a podtržítko `_`.
- Název proměnné musí začínat písmenem nebo podtržítkem, nikdy číslicí.
- Název proměnné by měl být stručný a popisný, aby byl snadno čitelný a srozumitelný pro ostatní programátory.
Standardně se při pojmenování požívá angličtina a využívají se pouze malá písmena. U víceslovných názvů se slova oddělují podtržítkem `_`. Zkuste se vyhnout používání klíčových slov jako názvů proměnných v Pythonu, jako jsou například `if`, `while`, `int`, `True`, `class`, `def`, `list`.

### Datový typ
Datový typ definuje, jaké druhy hodnot lze uložit do proměnné. Konkrétně určuje, jaký typ dat může být uložen v paměti počítače. Každý programovací jazyk má své vlastní datové typy, například celá čísla (integer), reálná čísla (float), textové řetězce (string), pole (array). Používání správných datových typů je důležité pro korektní běh programu a tvorbu efektivních a bezpečných aplikací.

### Operace s proměnnými
S proměnnými lze provádět několik základních operací. Ne všechny operace lze provádět nad všemi datovými typy. Nad číselnými proměnnými můžeme provádět matematické operace s klasickým způsobem (sčítání `+`, odčítání `-`, násobení `*`, dělení `/`, mocnění `**`, celočíselné dělení `//`). Operaci `+` lze použít také na typ string, kde funguje jako řetězení. Protože Python není typovaný jazyk, je na programátorovi, aby věděl, jaký datový typ je v proměnné uložený. Python při přiřazení nové hodnoty umožňuje vložit hodnotu jiného datového typu. V případě, že se pokusíme provést operaci, která na dané kombinaci typů není podporována editor nás upozorní červenou značkou před číslem řádku a chybovou zprávou.

<p align="center">
  <img src=/img/spatneTypy.png alt="Operace na nepodporované kombinaci typů width="100%">
  <em>Operace na nepodporované kombinaci typů</em>
</p>

Pokud na proměnných provádíme nějakou operaci, je pravděpodobné, že s ní budeme chtít dále pracovat, nezapomeňte ji proto uložit do proměnné, můžete vytvořit novou nebo přepsat hodnotu již existující.

## Úloha 1 - Proměnné, Fibonacciho posloupnost <a name="assignment1"/>
### Zadání
Napište program, který bude v nekonečném cyklu `while True` počítat Fibonaccioho posloupnost a vypisovat její výpočet na micro:bit (použijte metodu `scroll`obdobně jako v minulé lekci). Program bude obsahovat tři proměnné – dva sčítance a výsledek. Proměnné vhodně pojmenujte. První výpis bude vypadat následovně: `0``+``1``=``1`
**Tip1:** Fibonacciho posloupnost je posloupnost čísel, kde každé číslo v posloupnosti je součtem dvou předchozích čísel. Začíná se obvykle číslem 0 a následuje číslo 1. Další číslo je poté součtem 0 a 1, tedy 1, další je 1 + 1, tedy 2, další je 1 + 2, tedy 3, a tak dále. Takto pokračuje posloupnost dál do nekonečna.
**Tip2:** Metoda `scroll` bere jako parametr `string`, pro přetypování proměnné typu `int` využijet funkci `str()`.

### Co budete potřebovat
K této úloze nejsou potřeba žádné senzory a moduly.
### Co se naučíte
Cílem úlohy je vyzkoušet si práci s proměnnými a vybranou operací nad datovým typem `int`. Zároveň si žáci zopakují práci s editorem a micro:bitem z minulé lekce.
### Jak postupovat


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
### Diagram
```mermaid
  graph TD;
      A[Start] --> B[number1 = 0];
      B --> C[number2 = 0];
      C --> D{Is it True?};
      D -- YES --> E[sum = number1 + number2];
          E --> F[vypis vypocet na displej tvaru 'sum = number1 + number2'];
          F --> G[number1 = number2];
          G --> H[number2 = sum];
          H --> D;
```
### Popis vzorové implementace
Na řádcích 3 a 4 jsou vytvořené proměnné, do kterých jsou uložené výchozí hodnoty Fibonacciho posloupnosti 0 a 1. Zbytek programu je obalený v nekonečném while cyklu. Na řádku 7 je do proměnné `sum` přiřazen součet dvou předchozích členů posloupnosti, které jsou uložené v proměnných `number1` a `number2`. 

Metoda `scroll` zavolaná na objektu display postupně zobrazuje výpočet a výsledek na micro:bit. Protože `scroll` bere pouze argumenty typu string přetypujte proměnné `number1` a `number2` pomocí funkce `str()`. Aplikace operace `+` na hodnoty typu string funguje jako řetězení (konkatenace).
Na řádku 9 je do proměnné `number1` uložena hodnota proměnné `number2`, na řádku 10 je do proměnné `number2` uložena hodnota z proměnné `sum`. Tato změna hodnot v proměnných umožňuje v další iteraci vypočítat následující hodnotu Fibonacciho posloupnosti.

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



## Úloha 2 - Seznámení s Nezha kitem, Fibonacciho posloupnost <a name="assignment2"/>
### Zadání
Použijte již vytvořený program a modifikujte ho tak, aby rozsvítil na matrix modulu diody, jejichž pořadí odpovídá hodnotám Fibonacciho posloupnosti. Naimportujte modul obsahující metody a funkce pro matrix display a využijte jeho metodu `set_matrix_draw_index()`.
### Co budete potřebovat
Pro tuto úlohu bude potřeba modul Nezha a PlanetX matrix modul.
### Co se naučíte
Cílem této úlohy je vyzkoušet použití Nezha kitu a import modulu jednoho z displejů.
### Jak postupovat
Nejprve naimportujte s žáky modul `matrix.py`. V levém spodním rohu editoru zvolte `Open` a vyberte v adresářové struktuře modul. Poté je důležité zvolit `Add file matrix.py`. Jako výchozí hodnota je zvoleno `Replace main code with matrix.py`, tím byste si přepsali kód, který se nachází v souboru `main.py`.

Jako další krok importujte modul matrix stejným způsobem, jako je naimportován modul microbit, tedy příkazem `from matrix import *`. Dále do proměnné `matrix` přiřaďtě instanci třídy `MATRIX` příkazem `matrix = MATRIX()`. Žákům v tuto chvíli není třeba vysvětlovat, co přesně tento příkaz dělá, tomu se budeme věnovat v osmé lekci věnované modulům. Nyní je možné na objektu matrix volat metody z modulu. Jaké to jsou zjistíme z nápovědy IDE po napsání `matrix.`.

Pro rozsvícení diod na dané pozici modul obsahuje metodu `set_matrix_draw_index()`. Protože žáci ještě neznají práci s cykly a podmínkami, program skončí s výjimkou `ValueError`. Nicméně pokud diody svítí, znamená to, že se podařilo správně nahrát modul a upravit program.
### Vzorová implementace
```python
from microbit import *
from matrix import *

matrix = MATRIX()

number1 = 0
number2 = 1
sum = number1 + number2

while True:
    matrix.set_matrix_draw_index(sum-1)
    number1 = number2
    number2 = sum
    sum = number1 + number2
    sleep(500)
```
                                                          
### Diagram
```mermaid
  graph TD;
      A[Start] --> B[number1 = 0];
      B --> C[number2 = 1];
      C --> D[sum = number1 + number2];
      D --> E{Vejde se na displej?};
      E -- YES --> F[rozsvit bod v matici];
          F --> H[number1 = number2];
          H --> I[sum = number1 + number2];
          I --> J[vyckej 500 ms]
          J --> E
      E -- NO --> K[Konec]
```
### Popis vzorové implementace
TODO
### Doplňující poznámky 
TODO
## Shrnutí <a name="conclusion"/>
TODO
## Poznámky pro učitele <a name="pozn"/>
TODO
