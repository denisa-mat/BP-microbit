# Lekce 1
#### Úvod do algoritmizace a první program

## Obsah
[Motivace](#motivace)  
[Prostředky - MicroPython, algoritmus, micro:bit, IDE](#resources)  
[Úloha 1 - Hello World](#hello-world)  
[Shrnutí](#shrnuti)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
Otázky na úvod:
1. Jaká je Vaše zkušenost s programováním?
2. Co si myslíte, že programátor dělá?
3. K čemu je dobrá znalost programování a algoritmizace?

Představte si, že máte rutinní úkol, který vykonáváte pravidelně, vyžaduje pokaždé udělat stejný sled akcí a zabere vám nezanedbatelné množství času. Takový úkol je ideálním kandidátem pro automatizaci. Nezáleží na tom, v jakém oboru se nacházíme, automatizovat mnoho procesů a rutinních úkolů může ušetřit čas a zdroje ve všech odvětvích.

Znalost algoritmizace může být užitečná pro různé obory a profese, nejen pro přírodní a technické vědy. Například v oblasti ekonomie a financí je důležité umět navrhovat a vyhodnocovat algoritmy pro rozhodování v oblasti investic a řízení finančních toků. V oblasti obchodu a marketingu může být znalost algoritmů užitečná pro analýzu dat a vytváření efektivních strategií pro reklamu a prodej.

## Prostředky - MicroPython, algoritmus, micro:bit, IDE <a name="resources"/>

### Jazyk MicroPython
Žáci by se dle RVP měli na základní škole setkat s algoritmizací, k čemuž jsou, právě blokové jazyky vhodné a často využívané. Ukázka, jak daný kód vypadá v blocích, které již znají, značně usnadní přechod k Pythonu.

Python je vysokoúrovňový, interpretovaný programovací jazyk, který nabízí podporu pro různá programovací paradigmata. V případě micro:bitu si vystačíme s imperativním. Je dynamicky typovaný, a tedy by žáci po přechodu z bloků nemuseli mít zásadní problém. Syntaxe je založena na oddělování kódu pomocí bílých znaků, které oddělují jednotlivé bloky a přispívají k dobré čitelnosti. Zároveň tento způsob zápisu do jisté míry připomíná práci s bloky, které zapadají do sebe a tvoří podobnou strukturu.

Python je zvolen z mnoha důvodů. Jedním z nich je jednoduchá syntaxe. Například v porovnání s jazyky Java nebo C klade Python důraz na čitelnost a jednoduchost kódu. Stručná syntaxe jazyka umožňuje vyjadřovat mnohé koncepty v nižším počtu řádků kódu a udržovat tak v kódu přehlednost. I proto se stále více výzkumníků shoduje, že Python je vhodný programovací jazyk pro začátečníky. V Pythonu se žáci z počátku nemusí zabývat třídami, metodami a jinými složitějšími konstrukty.

### Algoritmus
Algoritmus je postup nebo soubor kroků, které jsou navrženy tak, aby řešily určitý problém nebo vykonávaly určitou úlohu. Algoritmus může být popsán jako postup instrukcí, které jsou navrženy tak, aby byly provedeny v určitém pořadí a řídily tok dat, aby bylo dosaženo určeného výstupu.

V informatice se algoritmus používá především k řešení problémů a ke vytváření programů. Dobře navržený algoritmus je maximálně efektivní, což umožňuje vykonávat úlohy v kratším čase. U algoritmů se proto často bere v úvahu rozlišuje časová a prostorová složitost.

Algoritmus se také používá jako nástroj pro analýzu a návrh procesů a systémů, protože umožňuje rozdělit složité problémy na menší části, které se snáze řeší.

#### Vlastnosti algoritmů

**Rezultativnost**: Algoritmus vždy vede k výsledku.

**Konečnost**: Algoritmus musí vždy skončit.

**Obecnost**: Algoritmus by měl být obecný, což znamená, že by měl být použitelný pro různé vstupy a podobné problémy.

**Jednoznačnost**: Algoritmus pro stejné vstupy poskytuje stejné výstupy. Výsledek je ovlivněn pouze vstupem.

#### Vývojový diagram
Vývojový diagram je grafické znázornění postupu algoritmu pomocí symbolů a propojení mezi nimi. Používá se jako nástroj pro plánování, návrh, dokumentaci v oblastech jako je vývoj softwaru, inženýrství a dalších odvětvích. Vývojový diagram pomáhá vizualizovat složité procesy nebo postupy a umožňuje snadnější identifikaci problémů, chyb a nedostatků v algoritmu nebo procesu. Diagram usnadňuje spolupráci a komunikaci mezi členy týmu, kteří se podílejí na vývoji a implementaci algoritmu. Při tvorbě vývojového diagramu je třeba myslet na jeho čitelnost a srozumitelnost pro všechny členy týmu. Proto je důležité používat jasně definované symboly a základní pravidla pro tvorbu diagramu, která jsou obecně uznávaná v oboru.
- oválné symboly označují počátek a konec programu
- symbol kosočtverce se používá pro větvení (v podmínkách a cyklech)
- pro vstupní a výstupní operace se používají rovnoběžníky
- všechny ostatní příkazy zapisujeme do obdélníků
- symboly propojujeme šipkami

<p align="center">
  <img src=/img/diagram1.png alt="diagram">
</p>

### Micro:Bit
Micro:bit je programovatelný mikropočítač, jeho velikost je pouze 4 x 5 cm, přesto však skýtá mnoho funkcí. Má vestavěný displej, dvě tlačítka a několik vestavěných senzorů, například gyroskop, nebo snímání dotyku. Další senzory je možné připojit.

Micro:bit lze programovat na široké škále zařízení bez ohledu na platformu, což snižuje požadavky na hardwarové i programové vybavení. Program se do Micro:bitu přenáší pomocí přiloženého micro USB kabelu nebo bezdrátové komunikace Bluetooth.

### IDE
Jako vhodný editor byl vybrán webový [python.microbit.org](python.microbit.org), se kterým budeme pracovat ve všech lekcích (podrobnosti výběru a další alternativy jsou popsány v kapitole 3.2 bakalářské práce).
Editor python.microbit.org má tlačítko pro snadný přenos kódu do micro:bitu, je přívětivý pro začínající programátory a snadno se používá. Výhodou python.microbit.org je simulátor micro:bitu, ovšem bez modulů. Další předností je panel reference neboli dokumentace, která umožňuje vyhledání kódu, klíčových slov nebo dokonce řídících struktur přímo v editoru. Navíc je ještě možné tento kód drag&drop nebo kopírováním přenést do editoru, upravit a ihned použít. Editor python.microbit.org je webová aplikace, která umožňuje spustit editor odkudkoli, což studentům usnadňuje samostudium.

## Úloha 1 - Hello World <a name="hello-world"/>
### Zadání
Napište program, který na vestavěný displej vypíše řetězec "Hello World". Následně program nahrajte do micro:bitu.
### Co budete potřebovat
K této úloze nejsou potřebné žádné senzory ani Nezha sada. Je však potřeba micro:bit a kabel pro přenesení programu. To již v dalších úlohách nebude zmiňováno.
### Co se naučíte
Cílem úlohy je především vytvoření prvního programu v MicroPythonu. Dále prakticky seznámit žáky s vývojovým prostředím (IDE) a micro:bitem. Žáci také nahrají první program z počítače do micro:bitu. 
### Jak postupovat
Do okna editoru naimportujte modul microbit pomocí příkazu `from microbit import *`. Tento zápis značí, že importujete vše co modul obsahuje. Symbol `*` lze nahradit za konkrétní funkci nebo metodu, pokud nepotřebujeme pracovat s celým modulem.

Protože se celý řetězec na maticový displej micro:bitu nevejde, využijte pro opětovná zobrazení, bez nutnosti restartování programu, nekonečný while cyklu do něhož příkaz obalte. Nekonečný cyklus má jednoduchou podmínku, která se splní vždy. Stačí tedy použít `while True`.

Do micro:bitu program z počítače nahrajte pomocí přiloženého micro USB kabelu. Ve spodní části obrazovky vyberte `Send to micro:bit`. Otevře se nápověda a poté okno s kompatibilními zařízeními. 

<p align="center">
  <img src=/img/send1.png alt="Jak připojit micro:bit" width="100%">
  <em>Jak připojit micro:bit</em>
</p>

Vyberte micro:bit a klikněte na tlačítko připojit, zobrazí se progress bar a program se nahraje do micro:bitu. Ve spodní části obrazovky uvidíte zprávu o tom, zda se nahrání podařilo. Nyní až do odpojení micro:bitu stačí pro nové nahrání vždy jen kliknout na tlačítko "Send to micro:bit". 

<p align="center">
  <img src=/img/send2.png alt=" Jak nahrát kód " width="100%">
  <em>Jak nahrát kód do micro:bitu</em>
</p>

Alternativní způsob je program stáhnout ve formátu .hex pomocí tlačítka stáhnout a nahrát na micro:bit jako na externí úložiště. 
### Vzorová implementace
```python
from microbit import *

while True:
    display.scroll("Hello World")
```
### Popis vzorové implementace
Na prvním řádku importujeme celý modul microbit. V tomto konkrétním případě lze import celého obsahu nahradit pouze importem objektu display, který pro tuto úlohu stačí. Na řádku tři vytváříme nekonečný cyklus v jehož těle voláme metodu `scroll()` na objektu `display`, které předáme jako parametr požadovaný textový řetězec "Hello World".

### Doplňující poznámky
Cykly budou žákům podrobněji vysvětleny až v lekci 4, do té doby si vystačíme s `while True`, pro neustálé opakování programu.
V případě zájmu si můžou žáci slovo `World` nahradit svým jménem.

## Shrnutí <a name="shrnuti"/>
V této lekci byly představeny nástroje se kterými bude následně pracováno ve všech lekcích. Bylo zde mnoho infomací, které budou sloužit jako opěrné body pro následující kapitoly.

Otázky k zopakování:
- Co je algoritmus a jaké má vlastnosti?
- Jaké symboly se standardně používají ve vývojovém diagramu?
- Jak se jmenuje použitý programovací jazyk?
- Jakým způsobem se do micro:bita nahrává program?

## Poznámky pro učitele <a name="pozn"/>
Pro začátek se žákům nezmiňujte o existenci tříd, objektů a metod. Budeme se tomu věnovat v pozdějších lekcích.

Micro:bit je možné díky webovému editoru programovat i přes telefon nebo tablet, v takovém případě pro nahrání programu do micro:bitu využijte připojení pomocí Bluetooth, není to však příliš doporučené.

Všechny informace o MicroPythonu lze nalézt v oficiální dokumentaci [docs.micropython.org](https://docs.micropython.org/en/latest/)
