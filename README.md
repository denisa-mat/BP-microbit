# Lekce 0
### Úvodem 

### Obsah
[Co se žáci naučí](#napln)  
[Co budete potřebovat](#potreby)  
[Časová náročnost](#cas)  
[Struktura materiálu](#struktura)  
[Jak vypadá struktura programu v MicroPythonu](#program)
<a name="napln"/>
## Co se žáci naučí
Cílem tohoto výukového materiálu je přiblížit žákům algortimizaci a programování. Materiál od nevyžaduje žádné předchozí znalosti Programování v Pythonu. Je vhodné, aby žáci byli z předchozího studia seznámeni s blokovým programováním, není to zcela nezbytné, ale v úvodu se jim budou některé věci lépe představovat. Obsah lekcí je sestaven tak, aby odpovídal požadavkům plynoucím z revidovaného RVP. Žáci by na konci měli znát základní programové řídící struktury. Budou schopni vytvořit a zapsat algortismus řešící daný problém, a na základě něho vytvoří program v jazyce Python využívající cykly, větvení, proměnné a seznamy. Žáci dokáží program dekomponovat na funkce s parametry a návratovými hodnotami.<a name="potreby"/>
## Co budete potřebovat
Ve všech lekcích budou žáci pracovat s micro:bitem, počítačem a webovým editorem microPythonu python.microbit.org. Spolu s micro:bitem bude využitá sada Nezha a v některých úlohách tři senzory planetX, které nejsou její součástí. Konkrétní potřebné senzory budou specifikovány u každé úlohy. 
<a name="cas"/>
## Časová náročnost
Každá lekce je tvořena pro dvě vyučovací hodiny, v ideálním případě následujících po sobě v jednom bloku, tedy 90 minut. Lekcí je vytvořeno deset a v nich dohromady XX úloh pro programování micro:bitu pomocí MicroPythonu. 
<a name="struktura"/>
## Struktura materiálu
### Motivace
...
### Prostředky - teoretická část
...
### Úloha X
#### Zadání
#### Popis řešení
#### Doplňující poznámky 
...
### Shrnutí
...
### Poznámky pro učitele
...
## Jak vypadá struktura programu v MicroPythonu

```python
from microbit import *

# Nasleduje nekonecny cyklus

while True:
    display.scroll('Hello World')
```

Na řádku 1 se importuje knihovna microbit, která obsahuje všechny funkce a metody potřebné pro práci s
micro:bitem. Tímto řádkem budou začínat všechny programy. V případě, kdy se bude pracovat se senzory, bude potřeba importovat i další moduly. Hvěznička značí, že se importuje vše, co knihovna obsahuje.
Znak # na začátku třetího řádku znamená, že se jedná o komentář. Komentáře nejsou součástí vykonávaného programu, slouží programátorům pro poznámky týkající se kódu.
Syntaxe pythonu používá k identifikaci zanoření odsazení pomocí daného počtu mezer/tabulátoru (v závislosti na IDE). Každý příkaz, který je zanořen je součástí kódu, který je o úroveň výše.
