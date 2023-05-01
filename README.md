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
Ve všech lekcích budou žáci pracovat s micro:bitem, počítačem a webovým editorem microPythonu [python.microbit.org](python.microbit.org). Spolu s micro:bitem bude využitá sada Nezha a v některých úlohách tři senzory planetX, které nejsou její součástí. Konkrétní potřebné senzory budou specifikovány u každé úlohy. 
<a name="cas"/>
## Časová náročnost
Každá lekce je tvořena pro dvě vyučovací hodiny, v ideálním případě následujících po sobě v jednom bloku, tedy 90 minut. Lekcí je vytvořeno deset a v nich dohromady XX úloh pro programování micro:bitu pomocí MicroPythonu. TODO
<a name="struktura"/>
## Struktura materiálu
### Motivace
Cílem je žáky motivovat, dodat jim energii k přemýšlení a soustředění. Ukázat jim, jak lze dovednosti, které se naučí, prakticky využít. Nelze předpokládat, že si žáci uvědomují důležitost lekcí. Je třeba ukázat přínos pro jejich potřeby.
### Prostředky - teoretická část
V teoretické části jsou žákům představeny základní prostředky, teorie, syntax programovacího jazyka a další teoretická východiska, které jsou potřebné pro řešení konkrétních problémů v dané lekci. Účelem je žákům dané koncepty vysvětlit jednoduše a srozumitelně. Stále je však kladen důraz na exaktnost předávané teorie. Snažíme se, aby tato část nebyla pouze frontálním výkladem, proto má v lekcích různé podoby.
### Úloha X
#### Zadání
Žáci dostanou konkrétní úkol nebo problém, který bude jejich úkolem vyřešit.
#### Co budete potřebovat
Soupis senzorů a případně dalších pomůcek, které jsou potřeba k úspěšnému zvládnutí úlohy.
#### Co se naučíte
Zde se dozvíte na jaké dovednosti se úloha zaměřuje a co je jejím cílem.
#### Vzorová implementace
#### Popis řešení
Obsahuje detailní popis vzorové implementace. Zaměřuje se především na koncepty, které jsou nové pro danou lekci.
#### Doplňující poznámky 
Poznámky k úloze mohou obsahovat časté potíže nebo například vylepšení programu pro rychlejší žáky.
### Shrnutí
Slouží k stručnému zopakování klíčových pojmů lekce a upevnění znalostí. Pro vyučujícího k ověření nabitých znalostí.
### Poznámky pro učitele
Další poznámky týkající se celé lekce

## Jak vypadá struktura programu v MicroPythonu

```python
from microbit import *

# Nasleduje nekonecny cyklus

while True:
    display.scroll("Hello World")
```

Na řádku 1 se importuje modul pro microbit, který obsahuje všechny funkce a metody potřebné pro práci s micro:bitem. Tímto řádkem budou začínat všechny programy. V případě, kdy se bude pracovat se senzory, bude potřeba importovat i další moduly. Symbol `*` značí, že se importuje vše, co modul obsahuje.

Znak `#` na začátku třetího řádku znamená, že se jedná o komentář. Komentáře nejsou součástí vykonávaného programu, slouží programátorům pro poznámky týkající se kódu.

Syntaxe pythonu používá k identifikaci zanoření odsazení pomocí daného počtu mezer/tabulátoru (v závislosti na IDE). Každý příkaz, který je zanořen je součástí kódu, který je o úroveň výše.
