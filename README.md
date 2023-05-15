# Lekce 4 - Složené podmínky
#### Složené podmínky

### Obsah
[Motivace](#motivace)  
[Prostředky I – Složené podmínky](#resources1)  
[Úloha 1 - Test plnoletosti](#assignment1)  
[Úloha 2 - Horská dráha](#assignment2)  

## Motivace
Složené podmínky umožňují kombinovat více jednoduchých podmínek do jedné. To umožňuje vytvářet sofistikovanější rozhodovací struktury a ovládat tok programu na základě více podmínek najednou. Také podporuje v rozvoj kritického myšlení a logického uvažování. 

Vyjadřuje složité logické vztahy: Složené podmínky umožňují žákům vyjádřit logické vztahy jako například AND (a), OR (nebo) a NOT (negace). To je důležité pro tvorbu komplexních logických podmínek, které odpovídají reálným situacím.

## Prostředky I - Složené podmínky <a name="resources1"/> 
V Pythonu se používají logické operátory pro kombinaci podmínek: `and`, `or` a operátor negace `not`.

Operátor `and` vrací `True`, pokud jsou obě podmínky pravdivé, jinak vrací `False`.
```python
if podmínka1 and podmínka2:
    # provede se, pokud jsou obě podmínky pravdivé
```

Operátor `or` vrací `True`, pokud alespoň jedna z podmínek je pravdivá, jinak vrací `False`.
```python
if podmínka1 or podmínka2:
    # provede se, pokud je alespoň jedna z podmínek pravdivá
```

Operátor `not` neguje pravdivostní hodnotu podmínky, tedy vrací `True`, pokud je podmínka nepravdivá, a `False`, pokud je podmínka pravdivá.
```python
if not podmínka1:
    # provede se, pokud je podmínka1 nepravdivá
```

Tyto logické operátory můžeme využít pro sestavení složitějších podmínek. Operátory a podmínky lze spojovat a pomocí závorek zanořovat, vyhodnocení podmínky začíná u levého nejvíce vnitřního výrazu a pokračuje postupně k vnějším výrazům.

## Úloha 2 - Test plnoletosti <a name="assignment2"/>
### Zadání
Napište program, který bude kontrolovat věk osoby zadaný pomocí modulu `button`. Když se stiskne `button C` přičte se jeden rok až dokud není zmáčknut `button D`, kterým se věk potvrdí. Po celou dobu zobrazujte aktuální věk na segmentovém displeji (`nixietube`). Pokud je věk potvrzen a osoba je mladší pěti let zobrazte smutného smajlíka (`Image.SAD`). Pokud je mladší než osmnáct zobrazte křížek (`Image.NO`), pokud už osoba oslavila osmnácté narozeniny zobrazte fajfku (`Image.YES`). 
### Co budete potřebovat
Pro tuto úlohu je potřeba modul `distance` z Nezha kitu a moduly `button` a `nixietube`, které nejsou součástí sady.
### Co se naučíte
Cílem úlohy je vyzkoušet práci s podmínkami.
### Jak postupovat
Dejte žákům k dispozici vzorovou implementaci, ideálně vytištěné na papíře a využijte metodu PRIMM. Nechte žáky odhadnout co program dělá, zatím jim nedávejte zadání. Žáci ve skupinách diskutují o fukci programu. Následně nechte žáky připojit moduly a kód spustit v editoru. Žáci diskutují ve skupinách, zda správně vyhodnotili, jak se bude program chovat. Případně rozeberou v čem se spletli a z jakého důvodu. Zadejte žákům otázku/úkol který slouží k důkladnému prozkoumání programu. Například:
- Je mi přesně 5, jaký dostanu výstup? (odhadněte bez spuštění s danou hodnotou)
- Co se stane, když zmáčknu obě tlačítka najednou?
- Co když budu držet tlačítko C dlouhou dobu?
- Jak by se program choval pokud by neobsahoval `sleep()`?
### Vzorová implementace
```python
from microbit import *
from distance import *
from nixietube import *
from button import *

nixietube = NIXIETUBE(J1)
button = BUTTON(J2)

age = 0
age_confirmed = False

while True:
    if age_confirmed:
        if age < 5:
            display.show(Image.SAD)
        elif age < 18:
            display.show(Image.NO)
        else:
            display.show(Image.YES)
    else:
        if button.C_is_pressed():
            age += 1
            sleep(300)
        elif button.D_is_pressed():
            age_confirmed = True
    nixietube.set_show_num(age)
```
<p align="center">
  <img src=/img/diagram3.png alt="diagram3">
</p>

### Popis vzorové implementace
Nejprve proveďte import modulů nixietube a button, z nichž následně vytvoříte objekty. Na řádcích 9 a 10 vytvořte pomocné proměnné pro věk a značku o potvrzení zadaného věku. Ve while cyklu kontrolujte, zda byl věk potvrzen pokud ano zobrazte dle výsledku příslušného smajlíka. Pokud věk potvrzen nebyl zkontrolujte, které tlačítko bylo zmačknuto. Při zmáčknutí tlačítka C přičtěte jedničku k věku, pokud bylo zmáčknuto D, nastavte značku o potvrzení na hodnotu `True`.
### Doplňující poznámky 
Pokud vynecháte `sleep()` přičte se jednička opakovaně, protože program stihne za dobu zmáčknutí tlačítka více opakování těla while cyklu.

## Úloha 3 - Horská dráha <a name="assignment3"/>
### Zadání
Naprogramujte micro:bita, tak aby na displej zobrazoval, zda může zájemce jít na horskou dráhu. Na horskou dráhu může zájemce jen pokud je mu alespoň 11 let nebo měří více než 125 centimetrů. Zkuste pro řešení využít kód z předcházející úlohy, věk a výška se bude načítat stejným způsobem, jako věk v předchozí úloze.
### Co budete potřebovat
K řešení úlohy jsou využívány moduly button a nixietube, které nejsou součástí Nezha kitu. Pokud je nemáte je možné nahradit button tlačítky přímo na micro:bitu a místo výpisu na segmentový displej hodnoty scrollovat na displeji micro:bita.
### Co se naučíte
Úloha se zaměřuje na složené a vnořené podmínky.
### Jak postupovat
Dejte studentům program z předchozí úlohy a nechte je modifikovat dle zadání. Žáci využívají, že v předchozích částech pochopili strukturu kódu a překlenou hranici mezi cizím kódem a částečně vlastním.
### Vzorová implementace
```python
from microbit import *
from nixietube import *
from button import *

nixietube = NIXIETUBE(J1)
button = BUTTON(J2)

age = 0
age_confirmed = False
height = 0
height_confirmed = False

while True:
    if age_confirmed and height_confirmed:
        if age <= 10 and height < 125:
            display.show(Image.NO)
        else:
            display.show(Image.YES)
    elif age_confirmed:
        if button.C_is_pressed():
            height += 5
            nixietube.set_show_num(height)
        elif button.D_is_pressed():
            height_confirmed = True
            nixietube.set_clear()
    else:
        if button.C_is_pressed():
            age += 1
            nixietube.set_show_num(age)
        elif button.D_is_pressed():
            age_confirmed = True
            nixietube.set_clear()
    sleep(150)
```
### Popis řešení
Podobně jako v minulé úloze naimportujte moduly a inicializujte objekty. Dále vytvořte pomocné proměnné. Zbytek kódu již bude v těle while cyklu. Kontrolujte, zda byl potvrzen pouze věk i výška, či ani jedno. Pokud bylo potvrzeno obojí zobrazte smajlíky dle zadání. Na řádcích 21 a 28 načítáme hodnotu do proměnné na základě zmáčknutí tlačítka C, v případě stisknutí tlačítka D je věk potvrzen. Na konci while cyklu využijte metodu sleep().
### Doplňující poznámky 
Pokud máte pocit, že je úloha příliš komplexní nastavte hodnotu výšky staticky na začátku programu. Pak stačí upravit podmínky a kód zůstane z větší části stejný jako v předchozí úloze.

Zbyde-li vám čas, nechte žáky vytvořit vlastní program, který bude testovat jiné hodnoty. 


## Shrnutí <a name="conclusion"/>
- Jaké jsou základní logické operátory pro kombinaci podmínek?
- Proč je vhodné znát složené podmínky a nestačí jednoduché?
- K čemu slouží funkce sleep()?

## Poznámky pro učitele <a name="pozn"/>
Operace AND, OR a NOT jsou v boolovské algebře jsou základními logickými operacemi, které se používají ke kombinování a transformaci logických hodnot. Booleovská algebra se zabývá algebraickými operacemi nad logickými hodnotami, používají se v mnoha oblastech informatiky a elektrotechniky, jako jsou návrh digitálních obvodů, programování, databázové dotazy a další.
