# Lekce 7
#### Seznamy, indexace, foreach

## Obsah
[Motivace](#motivace)  
[Prostředky - Seznamy, indexace, foreach ](#resources1)  
[Úloha 1 - Seznamy](#assignment1)  
[Úloha 2 - Memory test](#assignment2)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Seznamy jsou jednou z nejdůležitějších datových struktur, umožňují ukládat hodnoty a manipulovat s nimi, což je velmi užitečné v mnoha různých typech programů. Seznamy mohou být použity pro ukládání seznamů uživatelských vstupů, výsledků zpracování dat, seznamu položek k nákupu, seznamu přátel na sociální síti a mnoho dalších.
## Prostředky – Seznamy, indexace, foreach <a name="resources1"/>
V Pythonu jsou seznamy jedním z nejčastěji používaných datových typů. Seznam umožňuje ukládat a pracovat s více hodnotami najednou, které mohou být různých datových typů. Seznamy jsou v Pythonu reprezentovány hranatými závorkami `[ ]` a jednotlivé prvky jsou odděleny čárkami.

Například, zde je příklad vytvoření seznamu čísel:
```python
cisla = [1, 2, 3, 4, 5]
```
Seznamy mohou být prázdné, nebo mohou obsahovat libovolný počet prvků. 
V Pythonu můžeme seznamy procházet pomocí cyklu `for` prvek po prvku a s každým provést nějakou operaci. Zápis takového cyklu vypadá následovně:
```python
for cislo in cisla:
	print(cislo)
	# tady muzeme pracovat s promennou cislo, mimo cyklus neni dostupna
```
K prvkům seznamu lze přistupovat pomocí indexu. Index prvního prvku v seznamu je 0. Index může být i záporný, což znamená, že začíná od konce seznamu. Pokud chceme přistoupit k nějakému prvku seznamu pomocí indexu použijeme za názvem seznamu hranaté závorky s indexem. Například po tomto přiřazení
```python
hodnota_na_indexu = cisla[2]
```
je v proměnné `hodnota_na_indexu` uloženo číslo 3.

Kromě toho mohou být prvky seznamu přidávány, mazány a modifikovány. 
Nad seznamy lze provádět několik dalších operací:
- přidat prvek na konec seznamu `nazev_seznamu.append(prvek)`
- zjistit délku seznamu pomocí funkce `len(nazev_seznamu)`
- zjistit, zda je prvek v seznamu `prvek in nazev_seznamu`
- zjistit počet výskytů daného prvku `nazev_seznamu.count(prvek)`
- vybrat ze seznamu podseznam `nazev_seznamu[1:3]`
- odstranit ze seznamu poslední prvek a vrátit ho `nazev_seznamu.pop()`
## Úloha 1 - Seznamy <a name="assignment1"/>
### Zadání
Vytvořte vhodně pojmenovaný seznam délky, kterou si definujete v proměnné. Do seznamu pomocí `random.randint()` náhodně vygenerujte znaky "C" a "D". Poté nový seznam postupně zobrazte na displej micro:bitu.
### Co budete potřebovat
Pro tuto úlohu nejsou potřeba žádné moduly.
### Co se naučíte
Cílem úlohy je naučit žáky pracovat se seznamy. Vytvořit seznam, přidávat do něho prvky a procházet seznam pomocí hodnot. Úloha je přípravou pro úlohu dva.
### Jak postupovat
Tento úkol můžete vytvořit společně se studenty nebo je nechat pracovat samostatně. Pokud budou pracovat sami, nejprve vysvětlete jak funguje funkce `randint()`. Randint je funkce z knihovny `random`, proto je potřeba nejprve ji z modulu naimportovat. Randint generuje (pseudo)náhodné celočíselné hodnoty v určeném rozsahu. Syntaxe funkce randint je následující `random.randint(start, end)`, kde `start` a `end` jsou celočíselné hodnoty, které určují počátek a konec intervalu.

Aby bylo možné hodnoty přidávat do seznamu, je potřeba seznam nejprve vytvořit. Do proměnné `memory_test_size` si uložte požadovanou délku seznamu, která představuje náročnost testu. Následně ve for cyklu s počtem opakování `memory_test_size`, do vytvořeného seznamu metodou `append()` přidejte "C" nebo "D" podle aktuálně náhodně vygenerovaného čísla. Pro kontrolu vygenerovaného symbolu použijte jednoduchou `if`, `else` podmínku.

Nakonec projděte hodnoty memory listu a metodou `scroll()`, je zobrazte na displej micro:bita. Je pravděpodobné, že pokud budou žáci pracovat sami budou se jejich řešení více či méně lišit. Netrvejte na svém řešení, cest je mnoho a každý půjde na řešení jiným způsobem.

### Diagram
<p align="center">
  <img src=/img/diagram1.png alt="diagram1" width="100%">
</p>

### Vzorová implementace
```python
from microbit import *
from random import randint

memory_test_size = 6
memory_list = []

for _ in range(memory_test_size):
    random_value = randint(0,2)
    if random_value == 0:
        memory_list.append("C")
    else:
        memory_list.append("D")

for value in memory_list:
    display.scroll(value)
```

### Popis vzorové implementace
Po standardním importu modulu microbit následuje import funkce randint z modulu random. Na řádku 4 definujeme délku seznamu, na řádku 5 vytváříme prázdný seznam. Poté počítaným for cyklem do seznamu generujeme náhodné hodnoty a ty díky podmínce transformujeme na požadované hodnoty, které přidáváme do seznamu. V závěru opět metodou `scroll()`, zobrazíme hodnoty z listu postupně na displej.
### Doplňující poznámky 
Pro řešení této úlohy můžete využít některou z metod použitých v předchozích lekcích. Například kreslení diagramu, párové programování nebo PRIMM metodu.
## Úloha 2 - Memory test <a name="assignment3"/>
### Zadání
Úkolem je napsat program, který bude simulovat test paměti. V minulé úloze jste si nachystali náhodné generování seznamu. Nyní budete ověřovat, zda si uživatel zapamatoval sekvenci správně. Uživatel bude mačkat tlačítka z modulu button (označená C, D) v zobrazeném pořadí. Pokud zadá správně rozsvítí se červená LED dioda, pokud špatně tak zelená. Na konci programu se zobrazí na micro:bit emoji. V případě, že byla celá sekvence správně, zobrazte `Image.HAPPY`, jinak `Image.SAD`.
### Co budete potřebovat
Červenou a zelenou LED diodu a modul button. 
### Co se naučíte
Číst kód někoho jiného a sestavit program, který má více než pár řádků. Zároveň program obsahuje indexaci v seznamu a opakovaně využívá for cykly. 
### Jak postupovat
Tento úkol je zaměřen především na práci s programem. Žáci zde nebudou sami psát kód, ale skládat již připravené bloky. Úkol bude tak obtížný, na jak drobné části kód rozdělíte. Vezměte připravenou vzorovou implementaci a dejte žákům řádky či bloky kódu v nesprávném pořadí. Lze zvládnout v editoru, ale doporučujeme vytisknout, rozstříhat a zadat v papírové podobě. Úkolem žáků je program seskládat do funkčního kódu, který se bude chovat dle zadání. Následně nechte žáky program přepsat do editoru a vyzkoušet. Pokud narazí na chybu diskutujte, proč chybu udělali, zda by program sami napsali jinak.
### Vzorová implementace
```python
from microbit import *
from button import *
from led import *
from random import randint

button = BUTTON(J1)
green_led = LED(J2)
red_led = LED(J3)

memory_test_size = 6
memory_list = []

for _ in range(memory_test_size):
    random_value = randint(0,2)
    if random_value == 0:
        memory_list.append("C")
    else:
        memory_list.append("D")

for value in memory_list:
    display.scroll(value)

input_list = []

C_was_pressed = False
D_was_pressed = False
    
for i in range(memory_test_size):
    while not C_was_pressed and not D_was_pressed:
        C_was_pressed = button.C_is_pressed()
        D_was_pressed = button.D_is_pressed()
        
    if C_was_pressed: 
        input_list.append("C")
    elif D_was_pressed:
        input_list.append("D")
        
    if memory_list[i] == input_list[i]:
        green_led.set_led_on()
    else:
        red_led.set_led_on()
		
    sleep(600)
    C_was_pressed = False
    D_was_pressed = False
    red_led.set_led_off()
    green_led.set_led_off()
    
if memory_list == input_list:
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)
```
### Popis vzorové implementace
Část kódu následující po importech a vytvoření objektů následuje část programu, která je popsaná v úloze jedna. Na řádku 21 vytváříme prázdný seznam input_list, řádky 23 a 24 inicializují pomocné proměnné. Následuje for cyklus, v němž se vykonává hlavní část programu. nejprve na řádku 27 čekáme na stisknutí tlačítka, poté si uložíme, které tlačítko bylo zmáčknuto. Do seznamu input_list ukládáme "C" nebo "D" podle stisknutého tlačítka. Následně ověřujeme, jestli se hodnoty v seznamech na stejném indexu shodují a dle toho necháme rozsvítit příslušnou diodu. Nastavíme pomocné proměnné na výchozí stav, zhasneme led diody a ověřujeme podmínku for cyklu. Na závěr programu zobrazíme emoji podle toho, zda se odpovědi shodovali se zadáním.
### Doplňující poznámky 
Obtížnost přizpůsobíte schopnostem skupiny podle toho, na jak velké bloky program rozdělíte. Nejnáročnější varianta je rozdělit kód na samostatné řádky. Tato metoda umožňuje škálovat zadání, rychlejší skupině žáků lze dát program rozdělen na menší části, pomalejší nechat větší bloky. 
## Shrnutí <a name="conclusion"/>
- Jak v Pythonu značíme seznam?
- Jakým způsobem získáte ze seznamu třetí položku v pořadí?
- Jaké znáte operace nad seznamy?
## Poznámky pro učitele <a name="pozn"/>
Pseudonáhodné číslo, které vypadá jako náhodné, ale ve skutečnosti bylo vypočítáno pomocí matematického algoritmu. Tyto algoritmy jsou obvykle generovány na základě počátečního "seed" čísla, které je zpravidla odvozeno z aktuálního času nebo jiného proměnného parametru. Pseudonáhodné čísla jsou široce používána v počítačových simulacích, kryptografii, hraní her a dalších aplikacích.
