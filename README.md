# Lekce 2
#### Proměnné, datové typy

## Obsah
[Motivace](#motivace)  
[Prostředky - Proměnné, datové typy](#resources1)  
[Úloha 1 - Proměnné, výpis ](#assignment1)  
[Úloha 2 - Proměnné, Fibonacciho posloupnost ](#assignment1)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Setkali jste se někde s proměnnými?
Otázka má žáky navést k matematice a fyzice, kde se s proměnnými potkají v každé rovnici s neznámou. 

Proměnné jsou důležité pro matematické výpočty, například řešení rovnic, výpočet průměru a dalších matematických funkcí. Zjevné je také využití proměnných při vývoji her, kde mohou uchovávat informace o hráči, jako jsou jeho životy, skóre nebo stavové informace.

Dalším důležitým aspektem proměnných je, že umožňují programátorům vytvářet opakovaně použitelný kód a snižovat tak duplikaci kódu. Tím se zvyšuje efektivita vývoje a snižují se náklady na vývoj softwaru, protože zjednodušují práci programátorům.

## Prostředky - Proměnné, datové typy <a name="resources1"/>
### Proměnná
Proměnná je základní stavební kámen programování a označuje místo v paměti počítače, které je určeno pro ukládání hodnot. Proměnné mají název, datový typ a obsahují konkrétní hodnotu, která může být v průběhu programu měněna. Používají se pro ukládání vstupních dat, mezivýsledků a výstupních dat programu. Díky proměnným mohou programy uchovávat informace a provádět s nimi operace, což umožňuje tvorbu dynamických a interaktivních programů.

Pro přiřazení hodnoty do proměnné v Pythonu použijte operátor přiřazení `=` následovaný hodnotou, kterou chcete uložit do proměnné. Například:

```python
# přiřazení hodnoty 10 do proměnné x
x = 10

# přiřazení řetězce 'ahoj' do proměnné y
y = "ahoj"

# přiřazení logické hodnoty True do proměnné z
z = True
```
Při pojmenování proměnných v Pythonu dodržujte následující pravidla:
- Název proměnné může obsahovat pouze písmena (velká nebo malá), číslice a podtržítko `_`.
- Název proměnné musí začínat písmenem nebo podtržítkem, nikdy číslicí.
- Název proměnné by měl být stručný a popisný, aby byl snadno čitelný a srozumitelný pro ostatní programátory.
Standardně se při pojmenování požívá angličtina a využívají se pouze malá písmena. U víceslovných názvů se slova oddělují podtržítkem `_`. Vyhněte se používání klíčových slov jako názvů proměnných, jde například o `if`, `while`, `int`, `True`, `class`, `def`, `list`.

### Datový typ
Datový typ definuje, jaké druhy hodnot lze uložit do proměnné. Konkrétně určuje, jaký typ dat může být uložen v paměti počítače. Každý programovací jazyk má své vlastní datové typy, například celá čísla, reálná čísla, textové řetězce, pole. Používání správných datových typů je důležité pro korektní běh programu a tvorbu efektivních a bezpečných aplikací.

V Pythonu jsou tři základní datové typy

Číselné datové typy:

Python podporuje celá čísla `integer` a desetinná čísla `float`. Celá čísla slouží k reprezentaci celých čísel bez desetinné části, například `age = 25`. Desetinná čísla se používají pro reprezentaci čísel s desetinnou částí, například `pi = 3.14`

Řetězcový datový typ:

Řetězce jsou sekvence znaků, které mohou být považovány za text. Řetězce se v Pythonu zapisují uvozením jednoduchými `''` nebo dvojitými `""` uvozovkami. Příkladem je `name = 'John'`, kde je jméno John přiřazeno proměnné `name`.

Logický datový typ:

Logický datový typ může nabývat dvou hodnot: `True` (pravda) a `False` (nepravda). Tyto hodnoty se používají pro vyhodnocování logických výrazů a řízení toku programu na základě podmínek. Využívá k tomu základní logické operace Booleovy algebry, které jsou také aplikovány na logické datové typy.
- Konjunkce `AND`: Vrací `True` pouze tehdy, pokud jsou oba vstupní výrazy `True`, jinak vrací `False`.
- Disjunkce `OR`: Vrací `True`, pokud je alespoň jeden ze vstupních výrazů `True`, jinak vrací `False`.
- Negace `NOT`: Vrací opačnou hodnotu k vstupnímu výrazu. Pokud je vstupní výraz `True`, vrátí `False`, a naopak.

Dále můžeme používat rozšiřující datové typy, jako jsou `list` (seznam), `dictionary` (slovník) a `tuple` (n-tice). Tyto datové typy nám umožňují pracovat s kolekcemi hodnot a poskytují další flexibilitu a možnosti při programování.


### Operace s proměnnými
S proměnnými lze provádět několik základních operací. Ne všechny operace lze provádět nad všemi datovými typy. Nad číselnými proměnnými můžeme provádět matematické operace s klasickým způsobem (sčítání `+`, odčítání `-`, násobení `*`, dělení `/`, mocňování `**`, celočíselné dělení `//`). Operaci `+` lze použít také na typ `string`, kde funguje jako řetězení. Protože Python není typovaný jazyk, je na programátorovi, aby věděl, jaký datový typ je v proměnné uložený. Python při přiřazení nové hodnoty umožňuje vložit hodnotu jiného datového typu. V případě, že se pokusíme provést operaci, která na dané kombinaci typů není podporována editor nás upozorní červenou značkou před číslem řádku a chybovou zprávou.

<p align="center">
  <img src=/img/spatneTypy.png alt="Operace na nepodporované kombinaci typů" width="100%">
  <em>Operace na nepodporované kombinaci typů</em>
</p>

V Pythonu je také možné hodnoty přetypovat pomocí funkcí nebo metod určených pro daný datový typ. Základní funkce pro přetypování jsou:
- `int()`: Přetypuje hodnotu na celé číslo.
- `float()`: Přetypuje hodnotu na desetinné číslo.
- `str()`: Přetypuje hodnotu na řetězec.

Pokud na proměnných provádíme nějakou operaci, je pravděpodobné, že s ní budeme chtít dále pracovat, nezapomeňte ji proto uložit do proměnné, můžete vytvořit novou nebo přepsat hodnotu již existující.

## Úloha 1 - Proměnné, výpis <a name="assignment1"/>
### Zadání
Napište program, na jehož začátku do proměnných uložíte vaše jméno a věk a následně zobrazte postupně na displej text ve tvaru `Vase jmeno je Anonym a vek je 99 let.`
### Co budete potřebovat
K této úloze není potřeba kromě micro:bitu a kabelu pro přenesení programu žádný rozšiřující modul.
### Co se naučíte
Cílem úlohy je vyzkoušet si práci s proměnnými a datovými typy. Žáci si také zopakují práci s editorem a micro:bitem z minulé lekce.
### Jak postupovat
Nejprve si do proměnných uložte dané hodnoty a následně se pokuste řetězec vypsat. Pro výpis použijte metodu `display.show()`, která předejte požadovaný řetezec. Řetezce je možné sčítat, použijte tedy pro zřetězení operaci `+`. Pro výpis vynechejte diagritiku, micro:bit není schopen ji zobrazit. Nezapomeňte věk přetypovat na typ `string`. Přetypování je proces změny datového typu proměnné na jiný datový typ. V Pythonu je možné přetypování provést pomocí vestavěných funkcí, jako jsou `int()`, `float()`, `str()`. Je důležité mít na paměti, že některé datové typy nemohou být přetypovány na jiné typy a v takovém případě dojde k chybě při běhu programu. 
### Vzorová implementace
```python
from microbit import *

name = "Anonym"
age = 99

display.show("Vase jmeno je " + name + " a vek je " + 
             str(age) + " let.")
```

### Popis vzorové implementace
Na řádcích 3 a 4 jsou vytvořené proměnné, do kterých jsou uložené požadované hodnoty. Metoda `show()` zavolaná na objektu display postupně zobrazuje požadovaný text na micro:bit.

### Doplňující poznámky 
Pokud se pokusíte zobrazit znaky s diakritikou, místo požadovaného znaku uvidíte otazník. Zde je možnost s žáky probrat kódování.

## Úloha 2 - Proměnné, Fibonacciho posloupnost <a name="assignment1"/>
### Zadání
Napište program, který bude v nekonečném cyklu `while True` počítat Fibonacciho posloupnost a vypisovat její výpočet na micro:bit (použijte metodu `scroll` obdobně jako v minulé lekci). Program bude obsahovat tři proměnné – dva sčítance a výsledek. Proměnné vhodně pojmenujte. První výpis bude vypadat následovně: `0+1=1`

### Co budete potřebovat
K této úloze je potřeba jen micro:bit a kabel pro přenesení programu.
### Co se naučíte
Cílem úlohy je vyzkoušet si práci s proměnnými a vybranou operací nad datovým typem `int`. Zároveň si žáci zopakují práci s editorem a micro:bitem z minulé lekce.
### Jak postupovat
Nejprve zjistěte, zda žáci znají Fibonnaciho posloupnost a případně vysvětlete, že se jedná o posloupnost čísel, kde každé číslo v posloupnosti je součtem dvou předchozích čísel. Začíná se obvykle číslem 0 a následuje číslo 1. Další číslo je poté součtem 0 a 1, tedy 1, další je 1 + 1, tedy 2, další je 1 + 2, tedy 3, a tak dále. Takto pokračuje posloupnost až do nekonečna.

Zkuste s žáky probrat, jak bude program vypadat, co jsou jeho klíčové body. Můžete na tabuli spolu s žáky sestavit diagram podobně, jako je níže, to jim zjednoduší následné psaní kódu.

**K zamyšlení:**

- Kde budeme inicializovat proměnné? (V cyklu? Nad ním? Nebo někde jinde?)
- Podívejte se s žáky na metodu `scroll()`. Jaké bere parametry? Jakým způsobem ji zavoláme?

Metoda `scroll` bere jako parametr `string`, my jí však chceme dávat hodnotu typu `int`, musíme ji proto přetypovat. Pro přetypování proměnné typu `int` na `string` využijte funkci `str()`. Dejte žákům dostatek prostoru zkusit problém diskutovat a následně vyřešit.

### Diagram

<p align="center">
  <img src=/img/diagram1.png alt="diagram1" width="100%">
</p>

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

### Popis vzorové implementace
Na řádcích 3 a 4 jsou vytvořené proměnné, do kterých jsou uložené výchozí hodnoty Fibonacciho posloupnosti 0 a 1. Zbytek programu je obalený v nekonečném while cyklu. Na řádku 7 je do proměnné `sum` přiřazen součet dvou předchozích členů posloupnosti, které jsou uložené v proměnných `number1` a `number2`. 

Metoda `scroll` zavolaná na objektu display postupně zobrazuje výpočet a výsledek na micro:bit. Protože `scroll` akceptuje pouze argumenty typu string přetypujte proměnné `number1` a `number2` pomocí funkce `str()`. Aplikace operace `+` na hodnoty typu `string` funguje jako řetězení (konkatenace).
Na řádku 9 je do proměnné `number1` uložena hodnota proměnné `number2`, na řádku 10 je do proměnné `number2` uložena hodnota z proměnné `sum`. Tato změna hodnot v proměnných umožňuje v další iteraci vypočítat následující hodnotu Fibonacciho posloupnosti.

### Doplňující poznámky 
Fibonacciho posloupnost je poměrně jednoduchá posloupnost, ale má zásadní využití v řadě různých oblastí od přírodních věd až po design a umění. 

## Shrnutí <a name="conclusion"/>
- Co je to proměnná?
- Jak by měl vypadat název proměnné v Pythonu?
- Jaké znáte datové typy?
- Lze změnit datový typ? Pokud ano, jak?

## Poznámky pro učitele <a name="pozn"/>
Více o tom, jaké jsou v Pythonu jmenné konvence si můžete přečíst na [peps.python.org](https://peps.python.org/pep-0008/#introduction)
