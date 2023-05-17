# Lekce 0
#### Seznámení s materiálem

## Obsah
[Co se žáci naučí](#napln)  
[Co budete potřebovat](#potreby)  
[Časová náročnost](#cas)  
[Struktura materiálu](#struktura)  
[Jak vypadá struktura programu v MicroPythonu](#program)
<a name="napln"/>
## Co se žáci naučí
Cílem tohoto výukového materiálu je přiblížit žákům algoritmizaci a programování. Materiál od nevyžaduje žádné předchozí znalosti Programování v Pythonu. Je vhodné, aby žáci byli z předchozího studia seznámeni s blokovým programováním, není to zcela nezbytné, ale v úvodu se jim budou některé věci lépe představovat. 

Obsah lekcí je sestaven tak, aby odpovídal požadavkům plynoucím z revidovaného RVP. Žáci by na konci měli znát základní programové řídící struktury. Budou schopni vytvořit a zapsat algoritmus řešící daný problém, a na základě něho vytvoří program v jazyce Python využívající cykly, větvení, proměnné a seznamy. Žáci dokážou program dekomponovat na funkce s parametry a návratovými hodnotami.<a name="potreby"/>
## Co budete potřebovat
Ve všech lekcích budou žáci pracovat s micro:bitem, počítačem a webovým editorem microPythonu [python.microbit.org](python.microbit.org). Editor je možné používat ve všech běžně používaných prohlížečích, vzhledem k nahrávání programu micro:bitu doporučujeme použít Microsoft Edge, z něhož je nahrávání nejkomfortnější. Zároveň tento editor umožňuje instalovat web jako aplikaci. Díky tomu je možné mít pohodlně umístěnou ikonu a otevřít editor jedním kliknutím. 

Spolu s micro:bitem bude využitá sada Nezha. Sada se dá pořídit i s micro:bitem, nebo zakoupit zvlášť pokud už micro:bita máte. V některých úlohách se využívají tři senzory planetX, které nejsou její součástí. Jedná se o matrix displej, segment displej a button. Konkrétní potřebné senzory budou specifikovány u každé úlohy. Tyto rozšiřující senzory a displeje využívají moduly, které je třeba naimportovat.
<a name="cas"/>
## Časová náročnost
Každá lekce je tvořena pro dvě vyučovací hodiny, v ideálním případě následujících po sobě v jednom bloku, tedy 90 minut. Lekcí je vytvořeno deset a v nich dohromady XX úloh pro programování micro:bitu pomocí MicroPythonu. TODO
<a name="struktura"/>
## Struktura materiálu
### Motivace
Cílem je žáky motivovat, dodat jim energii k přemýšlení a soustředění. Ukázat jim, jak lze dovednosti, které se naučí, prakticky využít. Nelze předpokládat, že si žáci uvědomují důležitost lekcí. Je třeba ukázat přínos pro jejich potřeby.
### Teoretická část – Prostředky
V teoretické části jsou žákům představeny základní prostředky, teorie, syntax programovacího jazyka a další teoretická východiska, které jsou potřebné pro řešení konkrétních problémů v dané lekci. Účelem je žákům dané koncepty vysvětlit jednoduše a srozumitelně. Stále je však kladen důraz na exaktnost předávané teorie. Snažíme se, aby tato část nebyla pouze frontálním výkladem, proto má v lekcích různé podoby.
### Praktická část – Úloha X
#### Zadání
Žáci dostanou konkrétní úkol nebo problém, který bude jejich úkolem vyřešit.
#### Co budete potřebovat
Soupis senzorů a případně dalších pomůcek, které jsou potřeba k úspěšnému zvládnutí úlohy.
#### Co se naučíte
Zde se dozvíte, na jaké dovednosti se úloha zaměřuje a co je jejím cílem.
#### Jak postupovat
Popisuje konkrétní způsob, jak s danou úlohou pracovat. V některých kapitolách obsahuje také různé metody výuky.
#### Vzorová implementace
Zde bude jedna z možných implementací zadané úlohy.
#### Popis řešení
Obsahuje detailní popis vzorové implementace. Zaměřuje se především na koncepty, které jsou nové pro danou lekci.
#### Doplňující poznámky 
Poznámky k úloze mohou obsahovat časté potíže nebo například vylepšení programu pro rychlejší žáky.
### Shrnutí
Slouží k stručnému zopakování klíčových pojmů lekce a upevnění znalostí. Pro vyučujícího k ověření získaných znalostí.
### Poznámky pro učitele
Další poznámky týkající se celé lekce a odkazy na rozšiřující zdroje.
<a name="program"/>
## Struktura programu v MicroPythonu
```python
from microbit import *

# Nasleduje nekonecny cyklus

while True:
    display.scroll("Hello World")
```

Na řádku 1 se importuje modul pro micro:bit, který obsahuje všechny funkce a metody potřebné pro práci s micro:bitem. Znak `#` na začátku třetího řádku znamená, že se jedná o komentář. Komentáře nejsou součástí vykonávaného programu, slouží programátorům pro poznámky týkající se kódu.

Syntaxe pythonu používá k identifikaci zanoření odsazení pomocí daného počtu mezer/tabulátoru (v závislosti na IDE). Každý příkaz, který je zanořen je součástí kódu, který je o úroveň výše. Všechny další koncepty a principy budou vysvětleny v lekcích.
<a name="moduly"/>
## Moduly
Pro práci micro:bitem a rozšiřujícími senzory a displeji je potřeba naimportovat moduly. Moduly jsou způsob, jak organizovat kód, což umožňuje jeho znovupoužití a sdílení s ostatními programátory. Modul je soubor obsahující Python kód, který může být importován do jiných souborů Python kódu. Moduly mohou obsahovat funkce, třídy, proměnné, konstanty a další prvky, které chceme sdílet. Kromě vestavěných modulů si také můžeme vytvořit vlastní moduly a používat je ve svých projektech.

Moduly se v Pythonu obvykle importují pomocí klíčového slova `import`. Existují různé způsoby, jak importovat modul a jeho funkce, zde budeme importovat celé moduly pomocí příkazu `from nazev_modulu import *`, kde `*` značí import všeho, co modul obsahuje. Pokud bychom chtěli importovat pouze nějakou funkci z modulu, nahradíme `*` názvem dané funkce. Jak nahrát moduly, které nejsou dostupné z IDE bude vysvětleno ve třetí lekci předtím, než se s nimi bude poprvé pracovat. Pro úlohy, které jsou umístěné v těchto materiálech doporučuji využívat moduly z přiloženého adresáře. Pro snažší práci zde byla upravena dokumentace metod a některé byly přidány.

