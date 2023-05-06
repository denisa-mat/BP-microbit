# Lekce 5
### For cyklus
## Obsah
[Motivace](#motivace)    
[Prostředky I - For cyklus](#resources2)  
[Úloha 1 - For cykly ](#assignment1)  
[Úloha 2 - Odpočet ](#assignment2)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Přestože již žáci znají while cyklus, existují situace, ve kterých je for cyklus přirozenější a vhodnější volbou. Například při zpracování každého prvku v seznamu nebo při provádění určitých operací po pevně daný početkrát.

I když většinu programů využívající cykly, lze napsat pouze s využitím while cyklu, naučit se a pochopit for cyklus rozšiřuje váš repertoár nástrojů a umožňuje vám psát efektivnější a čitelnější kód ve vhodných situacích. For cyklus poskytuje jednodušší správu iterací. Nemusíte se starat o inicializaci proměnné, podmínku ukončení cyklu nebo inkrementaci, protože tyto kroky jsou automaticky zajištěny for cyklem.
## Prostředky II – For cyklus <a name="resources2"/>
For cyklus je další základní typ cyklu v programování, který slouží k procházení prvků v určité sekvenci, např. v seznamu, řetězci nebo množině, a opakování určitého bloku kódu pro každý prvek v této sekvenci. Tento cyklus se používá tam, kde známe předem počet opakování, nebo je potřeba provádět operace s každým prvkem v dané sekvenci.

Syntaxe for cyklu s daným rozsahem v Pythonu vypadá následovně:
```python
for prvek in range(0, 5):
    # blok kódu, který se opakuje, dokud je podmínka pravdivá
    # lze zde pracovat s promennou, ktera je aktualne v promenne prvek, napriklad:
    print(prvek) # do terminalu postupne vypise hodnoty 0, 1, 2, 3, 4
```
Funkce `range()`, bere hodnoty typu `int`, první číslo značí ostrý počátek intervalu (tedy včetně), druhé konec intervalu (pro zadanou hodnotu se již cyklus nevykoná). Je možné zadat ještě třetí parametr typu `int`, který umožňuje definovat krok. Pokud s proměnnou označující aktuální hodnotu nepotřebujeme pracovat místo názvu dáme `_`. 
## Úloha 1 - For cykly <a name="assignment1"/>
### Zadání
Úloha má tři části, každá část je jeden drobný úkol, zadání proto bude očíslované 1, 2, 3.
1. Napište program, který rozsvítí na matrix modulu postupně všechny diody. Začněte na indexu nula a skončete na indexu 127.
2. Napište program, který rozsvítí na matrix modulu postupně každou třetí diodu (první bude svítit druhá a třetí ne, čtvrtá zase ano).
3. Napište program, který na matrix modulu vytvoří rozsvícením diod šachovnici.
### Co budete potřebovat
Úloha je vytvořena pro maticový displej 8x16 bodů.
### Co se naučíte
Žáci si na jednotlivých úlohách vyzkouší různé varianty for cyklu.
### Jak postupovat
První dva úkoly jsou velmi podobné, nechte žáky se zamyslet v čem se liší a zjistit, co můžeme dát metodě `set_matrix_draw_index`. V třetím úkolu jde o zanoření dvou cyklů, pokud žáci zvládnou bez problému vyřešit první dva úkoly neměl by jim ani tento činit zásadní problémy. vysvětlete operaci modulo, která se pro tuto úlohu velmi hodí. Byť z matematiky žáci pravděpodobně neznají tento název, jedná se vlastně o zbytek po dělení. V informatice jde o velmi užitečnou a často používanou operaci. Celá část se zahodí a vrátí se pouze zbytek. Operaci modulo značíme symbolem procenta `%`. Hlídejte, aby si žáci při párovém programování ve svých dvojicích pravidelně střídali role.
### Vzorová implementace
1.     
```python
from microbit import *
from matrix import *

objekt_matrix = MATRIX()

for i in range(0, 128):
    matrix.set_matrix_draw_index(i)
    sleep(100)
    
```
2. 
```python
from microbit import *
from matrix import *

objekt_matrix = MATRIX()

for i in range(0, 128, 3):
    objekt_matrix.set_matrix_draw_index(i)
    sleep(100)
```
3. 
```python
from microbit import *
from matrix import *

objekt_matrix = MATRIX()

for column in range(0, 16):
    for row in range (0, 8):
        if (column % 2 == 0) and (row % 2 == 0):
            object_matrix.set_matrix_draw(column, row)
        elif (row % 2 == 1) and (column % 2 == 1):
            object_matrix.set_matrix_draw(column, row)
```

### Popis řešení
Naimportujeme modul pro maticový displej, stejně jako v předchozích lekcích. Následně vytvořte `objekt_matrix`. První a druhý úkol se liší pouze počtem parametrů, které jsou předány funkci `range()`. V prvním případě chceme rozsvítit všechny, zadáme tedy jen interval. Ve druhém chceme rozsvítit každý třetí, přidáme tedy další parametr, který určuje krok, tedy o kolik se zvyšuje hodnota v každém kroku iterace. Pokud není specifikováno, výchozí hodnota je 1.

Ve třetí úloze budeme zvlášť iterovat nad sloupci a zvlášť nad řádky. První cyklus představuje iterace nad sloupci. Zanořený cyklus představuje iteraci nad řádky. Rozsvítit chceme diody, které jsou na sloupci i řádku se sudým indexem nebo na sloupci i řádku s lichým indexem. 
### Doplňující poznámky 
Podmínky v posledním úkolu zde pro přehlednost uvádíme zvlášť, ale lze je spojit pomocí operátoru `or` do jedné.

Pokud jsou někteří žáci rychlejší mohou zkusit vykreslovat vlastní obrazce.

Zkuste experimentovat se složením dvojic. Je obvyklou praxí vytvářet páry nevyvážené, kdy jeden z dvojice je pokročilejší než druhý, tím se vzájemně obohatí.

## Úloha 2 - Odpočet <a name="assignment2"/>
### Zadání
Napište program, který bude simulovat start závodu. Nejprve rozsviťte červenou diodu. Poté pomocí for cyklu vypište na displej micro:bitu čísla 3, 2, 1 a následně rozsviťte zelenou diodu.
### Co budete potřebovat
V úloze se využívá zelená a červená led dioda.
### Co se naučíte
Úloha má za cíl procvičit for cyklus.
### Jak postupovat
Žáci si musí na začátku uvědomit, kolik opakování bude potřeba ve for cyklu a následně jakým způsobem v cyklu vypsat požadovaná čísla. Naveďte je k využití iterační proměnné cyklu a vhodnému odečítání. Následně už zbývá jen na vhodných místech rozsvítit a zhasnou diody.
### Vzorová implementace
1.     
```python
from microbit import *
from led.py import *

red_led_object = LED(J1)
red_led_object = LED(J2)

red_led_object.set_on()

for i in range(3):  
    display.scroll(3-i)

red_led_object.set_off()
green_led_object.set_on()
```

### Popis řešení
Naimportujeme modul pro LED diody, stejně jako v předchozích lekcích a vytvořte objekty pro obě diody. Na začátku programu rozsviťte červenou diodu. Ve for cyklu se třemi iteracemi zobrazte požadovaná čísla na displej tak, že od čísla tři odečtete iterační proměnnou, tím se bude číslo na výstupu snižovat. Již mimo cyklus rozsviťte červenou diodu a následně zasněte zelenou.
### Doplňující poznámky 
je možné, že některé z žáků nenapadne odečítat od tří a pokusí se to obejít pomocí kontroly iterační proměnné a dle toho vypsat. Pokuste se jim vysvětlit, že pokus by odpočet běžel například od sta, nebyla vhodná cesta.
## Shrnutí <a name="conclusion"/>
TODO
## Poznámky pro učitele <a name="pozn"/>
Více informací o tom, jak funguje for cyklus si můžete přečíst v [dokumentaci Pythonu](https://wiki.python.org/moin/ForLoop).
