# Moduly
V Pythonu jsou moduly soubory, které obsahují definice funkcí, tříd a proměnných, které lze použít v jiných programech. Moduly jsou používány pro organizaci kódu do logických bloků a pro znovupoužitelnost kódu.

Python má mnoho vestavěných modulů, jako jsou moduly pro práci s řetězci, soubory, datovými strukturami a sítěmi. Dále je možné si vytvořit vlastní moduly a použít je v různých projektech. Moduly jsou načítány pomocí příkazu "import". Například pro načtení modulu pro práci s micro:bitem se použije následující:
import microbit
případně naimportujeme vše
from microbit import *
nebo pouze konkrétní funkce foo pomocí
from microbit import foo 

## Distance
### Fyzická komponenta
Sonar:bit
https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05007.html
### Popis
Modul Sonar:bit dokáže určit vzdálenost objektu pomocí ultrazvukového senzoru. Když signál narazí na objekt, odrazí se a putuje zpět k sonaru. Na základě doby návratu signálu je schopen určit přibližnou vzdálenost. 
### Použití
Může být použit k předběžnému posouzení podmínek na silnici, když ovládáte auto na dálku.
### Dostupné metody
get_distance(self, unit=0)
  * Parametry: 
    * Jednotky (int), 0 pro metrické (centimetry), 1 pro imperiální (palce)
  * Návratová hodnota: 
    * Vzdálenost (float)
  * Popis: Spočítá a vrátí vzdálenost od objektu

## Matrix
### Fyzická komponenta
8x16 Matrix Module
https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05029.html
### Popis
Modul 8 x 16 Matrix je druh maticové obrazovky 8 x 16, která dokáže zobrazovat čísla, běžně používaná písmena a symboly s rolovací funkcí.
### Použití
Dá se využít pro zobrazení konkrétních bodů v souřadnicovém systému.
### Dostupné metody
set_matrix_clear(self)
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Zhasne všechny body matice

set_matrix_draw(self, x, y)
  * Parametry:
    * Index souřadnice x (int) v intervalu 0-15,
    * Index souřadnice y (int) v intervalu 0-7
  * Návratová hodnota: None
  * Popis: Rozsvítí diodu na daných souřadnicích

set_matrix_draw_position(self, position)
  * Parametry:
    * Pozice (int) v intervalu 0-128,
  * Návratová hodnota: None
  * Popis: Rozsvítí diodu na dané pozici dle řádků matice 

set_matrix_expression(self, emoji)
  * Parametry:
    * Name of emoji (str), platné hodnoty jsou: Neutral, Sad, Smile, Angry
  * Návratová hodnota: None
  * Popis: Rozsvítí diody a vytvoří obraz zadaného emoji 

## Nezha
### Fyzická komponenta
TODO
### Popis
TODO
### Použití
TODO
### Dostupné metody
set_motors(self, motor, speed)
  * Parametry:
    * Konektor (int), do kterého je připojen motor v intervalu 1-4
    * Rychlost (int) motoru v intervalu -100-100
  * Návratová hodnota: None
  * Popis: Nastaví rychlost danému motoru


set_servo(self, servo, angle)
  * Parametry:
    * Konektor (int), do kterého je připojeno servo v intervalu 1-4
    * Úhel (int) nákolu v intervalu 0-180
  * Návratová hodnota: None
  * Popis: ??? TODO


## Nixietube
### Fyzická komponenta
TODO
### Popis
TODO
### Použití
TODO
### Dostupné metody





https://www.elecfreaks.com/learn-en/microbitplanetX/index.html
