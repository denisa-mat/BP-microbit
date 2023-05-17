# Lekce 3
#### Nezha sada, větvení, podmínky a logické operátory

## Obsah
[Motivace](#motivace)  
[Prostředky I – Nezha kit](#resources1)  
[Úloha 1 - Parkovací asistent](#assignment1)  
[Prostředky II – Podmínky](#resources2)  
[Úloha 2 - Parkovací asistent](#assignment2)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  
<a name="motivace"/>
## Motivace 
Podmínky v programování umožňují řídit programový tok na základě různých vstupů, bez podmínek není program dynamický. Často je potřeba provést nějakou akci jen v případě, že nastala nějaká konkrétní situace, to se bez podmínek nepodaří. Znalost podmínek je základem pro mnoho pokročilých programovacích konceptů, jako jsou cykly a funkce.

## Prostředky I - Nezha kit <a name="resources1"/>
### NezhaKit
Nezha Inventors Kit je robotická stavebnice navržená pro micro:bit a je kompatibilní s jeho první i druhou verzí. Tato sada pro vynálezce obsahuje několik senzorů PlanetX, díky nimž je možné se sadou vytvořit desítky různých projektů. Další senzory se dají pořídit zvlášť. Základ setu tvoří Nezha modul pro umístění micro:bitu.

Pro propojení jednotlivých modulů jsou použity vodiče s konektory RJ11. Stačí zacvaknout a senzory jsou propojené s Nezhou a tedy i s micro:bitem. Propojení je snadné a spolehlivé. 

<p align="center">
  <img src=/img/moduly.png alt="Moduly využívané v lekcích" width="100%">
  <em>Moduly využívané v lekcích</em>
</p>

Další výhodou je kompatibilita Nezha kitu se stavebnicí lego a Fischertechnik. Sada je uložena v praktickém boxu, který obsahuje:
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

## Úloha 1 - Seznámení s Nezha kitem, Fibonacciho posloupnost <a name="assignment1"/>
### Zadání
Použijte program vyvtvořený v minulé lekci a modifikujte ho tak, aby rozsvítil na matrix modulu diody, jejichž pořadí odpovídá hodnotám Fibonacciho posloupnosti. Naimportujte modul obsahující metody a funkce pro matrix display a využijte jeho metodu `set_matrix_draw_index()`.
### Co budete potřebovat
Pro tuto úlohu bude potřeba modul Nezha a PlanetX matrix modul.
### Co se naučíte
Cílem této úlohy je vyzkoušet použití Nezha kitu a import modulu jednoho z displejů.
### Jak postupovat
Nejprve naimportujte s žáky modul `matrix.py`. V levém spodním rohu editoru zvolte `Open` a vyberte v adresářové struktuře modul. Poté je důležité zvolit `Add file matrix.py`. Jako výchozí hodnota je zvoleno `Replace main code with matrix.py`, tím byste si přepsali kód, který se nachází v souboru `main.py`.

<p align="center">
  <img src=/img/modulNahrat.png alt="Přidání modulů do projektu" width="100%">
  <em>Přidání modulů do projektu</em>
</p>

Jako další krok importujte modul matrix stejným způsobem, jako je naimportován modul microbit, tedy příkazem `from matrix import *`. Dále do proměnné `matrix` přiřaďtě instanci třídy `MATRIX` příkazem `matrix = MATRIX()`. Žákům v tuto chvíli není třeba vysvětlovat, co přesně tento příkaz dělá, tomu se budeme věnovat v desáté lekci, ve které se modulům budeme věnovat více. Nyní je možné na objektu matrix volat metody z modulu. Jaké to jsou zjistíme z nápovědy IDE po napsání `matrix.`.

Pro rozsvícení diod na dané pozici modul obsahuje metodu `set_matrix_draw_index()`. Žáci pravděpodobně do metody zadají proměnnou `sum`. Prodiskutujte s nimi, zda se zobrazují správné hodnoty, a čím by mohlo být způsobeno, že ne. První dioda má index nula, proto se jako první rozsvítí až druhá s indexem 1 a dále budou všechny o jednu posunuté. Vyřešit to lze snadno odečtením jedničky od proměnné `sum`, při předávání do metody.

Protože žáci ještě neznají práci s cykly a podmínkami, program skončí s výjimkou `ValueError`. Nicméně pokud diody svítí, znamená to, že se podařilo správně nahrát modul a upravit program. Funkce `sleep()` říká jak dlouho v milisekundách má na daném místě program pozastavit. Při práci s micro:bitem budeme `sleep()` používat poměrně často.

### Diagram

<p align="center">
  <img src=/img/diagram2.png alt="diagram2" width="100%">
</p>

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

### Popis vzorové implementace
Na řádcích 1 a 2 provádíme potřebné importy. Na řádku 4 inicializujeme objekt `matrix` jako instanci třídy `MATRIX()`. Následně inicializujeme proměnné. Inicializace je proces přiřazení počáteční hodnoty proměnné, objektu nebo datové struktury před dalším použitím. V nekonečném `while True` pomocí metody `set_matrix_draw_index()`, které předáme `sum - 1` rozsvítíme diodu na příslušné pozici. Dále aktualizujeme hodnoty proměnných a zavoláme `sleep(500)`, aby bylo na displeji vidět, jak se diody postupně rozsvítí.
### Doplňující poznámky 
Pokud by žáci projevili zájem o opravu kódu tak, aby nevyhazoval výjimku. Je třeba změnit podmínku ve while cyklu tak, aby se tělo cyklu vykonalo pouze je-li požadovaný index v rozsahu displeje. Displej má 128 diod v osmi řádcích a šestnácti sloupcích. podmínka by tedy byla `while sum < 128`.

## Prostředky II - Podmínky <a name="resources2"/>
Podmínky se používají k rozhodování, které akce má program vykonat v závislosti na nějakém vstupu nebo stavu. 
Pro zápis podmínky využíváme klíčová slova `if` (pokud), `elif` (zkratka pro else if) a `else` (jinak). Za if a elif následuje podmínka (výraz nebo proměnná typu `bool`), na jejímž vyhodnocení závisí pokračování programu.

Pokud je podmínka vyhodnocena jako `True` (pravda), program vykoná část kódu, která je podmíněna touto podmínkou. Pokud je podmínka vyhodnocena jako `False` (nepravda), program se posune k další podmínce uvedené za `elif`. Pokud ani jedna z podmínek neplatí a již nenásleduje žádná další, program se posune do bloku `else`, který obsahuje výrazy, které se provedou, pokud neplatí ani jedna z podmínek uvedených v `if` ani v `elif`. Program nemusí obsahovat `else` větev vůbec, pokud v případě nesplnění ani jedné z podmínek nechceme vykonávat nic. Je zde důležité dávat pozor na odsazení, dle odsazení Python rozhodne, který řádek vykonat.

Podmínky v Pythonu mají následující zápis:
```python
from microbit import * 

podminka1 = False
podminka2 = True

if podminka1:
	# kód, který se vykoná je-li splněna podminka1
	print("podminka1 splnena")
elif podminka2:
	# kód, který se vykoná je-li splněna podminka2
	print("podminka2 splnena")
else:
	# kód který se vykoná není li splněna žádná z předchozích podmínek
	print("podminky nesplneny")
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
- `in`: Zjišťuje, zda se první výraz nachází v druhém výrazu (seznamu, řetězci apod.).
- `not in`: Ověřuje, zda se první výraz nenachází v druhém výrazu.

## Úloha 2 - Parkovací asistent <a name="assignment2"/>
### Zadání
Vytvořte simulaci parkovacího asistenta. Napište program, který bude pomocí senzoru pro snímání vzdálenosti hlídat, jak daleko je překážka a tuto vzdálenost vypíše na segmentový displej (nixietube). Pokud je vzdálenost menší než 20, pak rozsviďte červenou led diodu.
### Co budete potřebovat
Úloha využívá moduly distance a červenou led diodu ze sady Nezha a nixietube modul, který není součástí sady.
### Co se naučíte
Cílem úlohy je prakticky vyzkoušet jednoduchou podmínku obsahující pouze `if` a `else` větev.
### Jak postupovat
Úlohu začněte kresbou diagramu, poté pracujte dohromady se studenty, nechte si od nich radit.
Můžte použít návodné otázky:
- Jaké moduly je potřeba naimportovat?
- Jak budete volat metody z modulů?
- Skončí program někdy?

Při vytváření proměnných distance a nixietube jako parametr předáváme J1 - J4 dle konektoru v němž je modul zapojen. Vyvětlete studentům proč při ukládání do proměnné `dist` dělíte hodnotu celočíselně jednou. Metoda `set_show_number()` bere jako argument celé číslo typu `int`, metoda `get_distance()` vrací `double`, který na `int` nelze přetypovat, dělením dosteme hodnotu typu `float`, kterou už přetypovat lze. Následují jednoduché podmínky. Kdy chcete aby se dioda rozsvítila? Když je vzdálenost menší než 20 centimetrů, jinak ji zhasněte. Aby dioda změsile neblikala použijte `sleep(300)`.

### Diagram
<p align="center">
  <img src=/img/diagram2.png alt="diagram2">
</p>

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

### Popis vzorové implementace
Po úvodních importech jsou na řádcích 6, 7 a 8 inicializované objekty příslušných tříd. Jako parametr předáváme J1 - J4 dle konektoru v němž je modul zapojen. Uvnitř nekonečného cyklu nejprve zjišťujeme vzdálenost od překážky, kterou celočíselně dělíme jedničkou abychom získali hodnotu typu `float` s nulovou destinnou částí. Na řádku 12 hodnotu přetypovanou na `integer` pomocí metody `int()` zobrazujeme na segmentovém displeji. Dále kontrolujeme zda je vzdálenost menší než 20, pokud ano rozsvítíme led diodu metodou `set_led_on()`, jinak ji zhasneme zavoláním metody `set_led_off()`.

### Doplňující poznámky 
Je vhodné zmínit, možnost zavést si před cyklem proměnnou do níž uložíme požadovanou vzdálenost, kdy má dioda začít svítit. V přípdě dalšího programu v němž by se hodnota opakovala se bude lépe měnit hodnota. Změna proběhne pouze na jednom místě. Navíc je čitelnější co dané číslo znamená.

## Shrnutí <a name="conclusion"/>
- Jak nahrát modul pro ovládání displejů a senzorů do projektu?
- Jak se připojují senzory k NezhaKitu potažmo k micro:bitu?
- Jaké znáte operace pro srovnání hodnot v proměnných

## Poznámky pro učitele <a name="pozn"/>
Oficiální infomace k Nezha kitu naleznete na [elecfreaks.com](https://www.elecfreaks.com/learn-en/microbitKit/Nezha_Inventor_s_kit_for_microbit/Nezha-Inventor-s-kit-for-microbit.html).
