# Lekce 3 - Podmínky
### If, elif, else, logické operátory

### Obsah
[Motivace](#motivace)  
[Prostředky I – Podmínky](#resources1)  
[Úloha 1 - Parkovací asistent](#assignment1)  
[Prostředky II – Složené podmínky](#resources2)  
[Úloha 2 - Test plnoletosti](#assignment2)  
[Úloha 3 - Horská dráha](#assignment3)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  
<a name="motivace"/>
## Motivace 
Podmínky v programování umožňují řídit programový tok na základě různých vstupů, bez podmínek není program dynamický. Často je potřeba provést nějakou akci jen v případě, že nastala nějaká konkrétní situace, to se bez podmínek nepodaří. Znalost podmínek je základem pro mnoho pokročilých programovacích konceptů, jako jsou cykly a funkce.
<a name="resources1"/>
## Prostředky I - Podmínky
Podmínky se používají k rozhodování, které akce má program vykonat v závislosti na nějakém vstupu nebo stavu. 
Pro zápis podmínky využíváme klíčová slova `if` (pokud), `elif` - zkratka pro else if,  `else` (jinak). Za if a elif následuje podmínka (výraz nebo proměnná typu bool) dle toho, jak se vyhodnotí program pokračuje.

Pokud je podmínka vyhodnocena jako `True` (pravda), program vykoná část kódu, která je podmíněna touto podmínkou. Pokud je podmínka vyhodnocena jako `False` (nepravda), program se posune k další podmínce uvedené za `elif`. Pokud ani jedna z podmínek neplatí a již nenásleduje žádná další, program se posune do bloku `else`, který obsahuje výrazy, které se provedou, pokud neplatí ani jedna z podmínek uvedených v `if` ani v `elif`. Program nemusí obsahovat `else` větev vůbec, pokud v případě nesplnění ani jedné z podmínek nechceme vykonávat nic. Je zde důležité dávat pozor na odsazení, dle odsazení Python rozhodne, který řádek vykonat.

Podmínky v Pythonu mají následující zápis:
```python
from microbit import * 

podminka1 = False
podminka2 = True

if podminka1:
	print("podminka1 splnena")
	# kód, který se vykoná je-li splněna podminka1
elif podminka2:
	print("podminka2 splnena")
	# kód, který se vykoná je-li splněna podminka2
else:
	print("podminky nesplneny")
	# kód který se vykoná není li splněna žádná z předchozích podmínek
# zbytek programu
```
<p align="center">
  <img src=/img/diagram1.png alt="diagram1">
</p>

V Pythonu se používají následující operátory pro srovnávání hodnot a výrazů:

- `==` (rovná se): Porovnává, zda jsou dva výrazy rovny.
- `!=` (nerovná se): Porovnává, zda jsou dva výrazy nerovnající se.
- `<` (menší než): Porovnává, zda je první výraz menší než druhý výraz.
- `>` (větší než): Porovnává, zda je první výraz větší než druhý výraz.
- `<=` (menší nebo rovno): Porovnává, zda je první výraz menší nebo roven druhému výrazu.
- `>=` (větší nebo rovno): Porovnává, zda je první výraz větší nebo roven druhému výrazu.
- `in`: Porovnává, zda se první výraz nachází v druhém výrazu (seznamu, řetězci apod.).
- `not in`: Porovnává, zda se první výraz nenachází v druhém výrazu.

## Úloha 1 - Parkovací asistent <a name="assignment1"/>
### Zadání
Vytvořte simulaci parkovacího asistenta. Napište program, který bude pomocí senzoru pro snímání vzdálenosti hlídat, jak daleko je překážka a tuto vzdálenost vypíše na segmentový displej (nixietube). Pokud je vzdálenost menší než 20, pak rozsviďte červenou led diodu.
### Co budete potřebovat
Úloha využívá moduly distance a červenou led diodu ze sady Nezha a nixietube modul, který není součástí sady.
### Co se naučíte
Cílem úlohy je prakticky vyzkoušet jednoduchou podmínku obsahující pouze if a else větev.
### Jak postupovat
Úlohu začněte kresbou diagramu, poté pracujte dohromady se studenty, nechte si d nich radit.
Můžte použít návodné otázky:
- Jaké moduly je potřeba naimportovat?
- Jak budete volat metody z modulů?
- Skončí program někdy?

Vyvětlete studentům proč při ukládání do porměnné `dist` dělíte hodnotu celočíselně jednou. Metoda `set_show_number()` bere jako argument celé číslo typu `int`, metoda `get_distance()` vrací `double`, který na `int` nelze přetypovat, dělením dosteme hodnotu typu `float`, kterou už přetypovat lze. Následují jednoduché podmínky. Kdy chcete aby se dioda rozsvítila? Když je vzdálenost menší než 20 centimetrů, jinak ji zhasněte. Aby dioda změsile neblikala použijte `sleep(300)`.
### Vzorová implementace
```python
from microbit import *
from distance import *
from nixietube import *
from led import *

distance = DISTANCE(J1)
nixietube = NIXIETUBE(J2)
led = LED(J3)

while True:
    dist = (distance.get_distance())//1
    nixietube.set_show_num(int(dist))
    if dist < 20:
        led.set_led_on()
    else:
        led.set_led_off()
    sleep(300)
```
### Diagram
<p align="center">
  <img src=/img/diagram2.png alt="diagram2">
</p>

### Popis vzorové implementace
Po úvodních importech jsou na řádcích 6, 7 a 8 inicializované objekty příslušných tříd. Jako parametr předáváme J1 - J4 dle konektoru v němž je modul zapojen. Uvnitř nekonečného cyklu nejprve zjišťujeme vzdálenost od překážky, kterou celočíselně dělíme jedničkou abychom získali hodnotu typu `float` s nulovou destinnou částí. Na řádku 12 hodnotu přetypovanou na `integer` pomocí metody `int()` zobrazujeme na segmentovém displeji. Dále kontrolujeme zda je vzdálenost menší než 20, pokud ano rozsvítíme led diodu metodou `set_led_on()`, jinak ji zhasneme zavoláním metody `set_led_off()`.
### Doplňující poznámky 
Je vhodné zmínit, možnost zavést si ořed cyklem porměnnou do níž uložíme požadovanou vzdálenost, kdy má dioda začít svítit. V přípdě dalšího programu v němž by se hodnota opakovala se bude lépe měnit hodnota. Změna proběhne pouze na jednom místě. Navíc je čitelnější co dané číslo znamená.

## Prostředky II - Složené podmínky <a name="resources2"/> 
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
- Co se stane, když zmáčku obe tlačítka najednou?
- Co když budu držet talčítko C dlouhou dobu?
- Jak by se prorgam choval pokud by neobsahoval `sleep()`?
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
Nejprve proveďte import modulů nixietube a button, z nichž následně vytvoříte objekty. Na řádcích 9 a 10 vytvořte pomocné proměnné pro věk a značku o potvrzení zadaného věku. Ve while cyklu kontrolujte, zda byl věk potvrzen pokud ano zobrazte dle výsedku příslušného smajlíka. Pokud věk potvrzen nebyl zkontrolujte, které tlačítko bylo zmačknuto. Při zmáčknutí tlačítka C přičtěte jedničku k věku, pokud bylo zmáčknuto D, nastavte značku o potvrzení na hodnotu `True`.
### Doplňující poznámky 
Pokud vznecháte `sleep()` přičte se jednička opakovaně, protože program stihne za dobu zmáčknutí tlačítka více opakování těla while cyklu.

## Úloha 3 - Horská dráha <a name="assignment3"/>
### Zadání
Naprogramujte microbita, tak aby na displej zobrazoval, zda může zájemce jít na horskou dráhu. Na horskou dráhu může zájemce jen pokud je mu alespoň 11 let nebo měří více než 125 centimetrů. Zkuste pro řešení využít kód z předcházející úlohy, věk a výška se bude načítat stejným způsobem, jako věk v předchozí úloze.
### Co budete potřebovat
K řešení úlohy jsou využívány moduly button a nixietube, které nejsou součástí Nezha kitu. Pokud je nemáte je možné nahradit button tlačítky přímo na micro:bitu a místo výpisu na segmentový dislej hodnoty scrollovat na displeji micro:bita.
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
Podobně jako v minulé úloze naimportujte moduly a inicializujte objekty. Dále vytvořte pomocné proměnné. Zbytek kódu již bude v těle while cyklu. Kontrolujete zda byl potvrzen pouze věk i výška, či ani jedno. Pokud bylo potvrzeno obojí zobrazte smajlíky dle zadání. Na řádcích 21 a 28 načítáme hodnotu do proměnné na základě zmáčknutí tlačítka C, v případě stisknutí tlačítka D je věk potvrzen. Na konci while cyklu využijte metodu sleep().
### Doplňující poznámky 
Pokud máte pocit, že je úloha příliš komplexní nastavte hodnotu výšky staticky na začátku porgramu. Pak stačí upravit podmínky a kód zůstane z větší části stejný jako v předchozí úloze.

Zbyde-li vám čas, nechte žáky vytvořit vlastní porgram, který bude testovat jiné hodnoty. 
<a name="conclusion"/>
## Shrnutí 
TODO
<a name="pozn"/>
## Poznámky pro učitele 
Operace AND, OR a NOT jsou v boolovské algebře jsou základními logickými operacemi, které se používají ke kombinování a transformaci logických hodnot. Booleovská algebra se zabývá algebraickými operacemi nad logickými hodnotami, používají se v mnoha oblastech informatiky a elektrotechniky, jako jsou návrh digitálních obvodů, programování, databázové dotazy a další.
