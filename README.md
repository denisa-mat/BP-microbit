# Lekce 4
### While cyklus

## Obsah
[Motivace](#motivace)  
[Prostředky I - While cyklus](#resources1)  
[Úloha 1 - Auto](#assignment1)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Cykly obecně umožňují značně zkrátit kód. Vše, co bychom jinak museli psát několikrát lze cyklem zopakovat třeba milionkrát nebo pracovat se vstupy a situacemi různé, předem neznámé délky. Pokud bychom programy, které jsme již vytvořili neměli obalené v nekonečném cyklu, provedla by se pouze jedna iterace a program by skončil. Cykly umožňují programátorům snadno implementovat opakující se procesy a zpracovat velké množství dat pomocí malého množství kódu.
## Prostředky I – While cyklus <a name="resources1"/>
While cyklus využívá podmínky, čímž plynule navazuje na předchozí lekci. Má také podobnou syntax. While cyklus se používá k řešení situací, kdy nevíme přesně, kolikrát bude třeba provést určitou akci. Smyslem cyklů je opakování zanořeného bloku kódu, dokud je podmínka splněna. Není-li podmínka splněna již v první iteraci, blok kódu se vůbec nevykoná.
Zápis while cyklu vypadá následovně:
```python=
while podmínka:
    # blok kódu, který se opakuje, dokud je podmínka pravdivá
# blok kódu, kde program pokračuje, když podmínka není pravdivá
```
I u cyklů je důležité dávat pozor na správné odsazení, bez toho nebude program fungovat správně.
Přestože jsme dosud pro zjednodušení používali nekonečný cyklus `while True`, od této chvíle je to něco, čemu se budeme chtít spíš vyhnout. Každý program má nějaký konečný stav, v němž chceme, aby skončil.
## Úloha 1 - Auto <a name="assignment1"/>
### Zadání
Sestavte ze Nezha sady vozidlo, které bude pohánět motor a v předu bude mít distance senzor a crash senzor. Poté ho naprogramujte tak, že pojede rychlostí `fast` dokud crash senzor nebude zmačknutý. Pokud bude vozidlo překážce blíže než 40 centimetrů zpomalí na rychlost `slow`. Auto pojede až do chvíle, než sepne crash senzor, v tu chvíli se zastaví a program skončí.
### Co budete potřebovat
Pro tuto úlohu si připravte crash senzor a distance senzor. Oba jsou součástí Nezha sady.
### Co se naučíte
Žáci si vyzkouší sestavit vlastního robota a naprogramovat ho s využitím while cyklu. Zároveň si vyzkouší, jaké je programovat ve dvojicích.
### Jak postupovat
Prvním krokem v této úloze je sestavit vozítko, které bude schopné pohybu vpřed a bude mít umístěný distance tak, aby mohl snímat vzdálenost od překážek a crash senzor tak, aby to byla první součástka, která do překážky narazí. Ukažte žákům motor a jak ho zapojit. Vymezte žákům na stavbu přesný čas, jinak hrozí, že budou celou hodinu stavět, doporučujeme 30 minut.

<p align="center">
  <img src=/img/vozitko.png alt="Ukázka sestavených vozítek" width="100%">
  <em>Ukázka sestavených vozítek</em>
</p>

 V této lekci zkuste využít metodu párového programování, kdy jsou žáci rozdělení do dvojic a jeden z žáků ovládá klávesnici a myš, soustředí se na drobné kroky, které má před sebou a aktuálně neřeší větší problémy. Druhý žák je v roli pozorovatele a navigátora, kontroluje kód, v případě nejasností nebo pochybností je sdílí. Zároveň si udržuje přehled o struktuře a celistvosti kódu.

Nechte žáky ve dvojicích prozkoumat jaké metody jsou pro dané senzory dostupné a zamyslet se, jak by se mohly hodit při plnění zadání. Dohlížejte na dodržování metody párového programování. V případě, že některá dvojice nebude vědět, jak postupovat dále, zkuste sestavit diagram.
### Vzorová implementace
```python =
from microbit import *
from motor import *
from crash import *
from distance import *

motor = MOTOR(1)
crash = CRASH(J1)
distance = DISTANCE(J2)

while not crash.crash_is_pressed():
    dist = distance.get_distance()
    if dist < 40:
        motor.set_motor_forward_slow()
    else:
        motor.set_motor_forward_fast()
motor.set_motor_stop()
```
### Diagram

<p align="center">
  <img src=/img/diagram1.png alt="diagram1" width="100%">
</p>

### Popis řešení
Provedeme potřebné importy modulů a vytvoříme instance daných tříd. Na řádku 10 vytvoříme cyklus s podmínkou, že není stisknut crash senzor. Uvnitř cyklu měříme vzdálenost a dle její hodnoty necháme auto zrychlit nebo zpomalit.
### Doplňující poznámky 
Pokud vozidlo couvá, přestože je nastavena jízda dopředu, umístili jste motor obraceným směrem. Není třeba motor otáčet, stačí vozidlo nastavit na opačný směr.

Else větev program obsahuje z důvodu nepřesnosti senzoru. Někdy senzor zaznamená velmi malou vzdálenost, přestože je od překážky daleko. Else větev zajistí, že se opět rozjede rychle.

Pro opětovné spuštění programu, který je nahrán micro:bitu použijte tlačítko na jeho zadní straně.

## Shrnutí <a name="conclusion"/>
TODO
## Poznámky pro učitele <a name="pozn"/>
Inspiraci pro stavbu vozítek můžete čerpat například na webu [elecfraks](https://www.elecfreaks.com/learn-en/microbitKit/Nezha_Inventor_s_kit_for_microbit/index.html). Je zde mnoho různých projektů, z nichž některé využívají pohybující se roboty.

