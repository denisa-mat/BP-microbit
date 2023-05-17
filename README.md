# Moduly
V Pythonu jsou moduly soubory, které obsahují definice funkcí, tříd a proměnných, které lze použít v jiných programech. Moduly jsou používány pro organizaci kódu do logických bloků a pro znovupoužitelnost kódu.

Python má mnoho vestavěných modulů, jako jsou moduly pro práci s řetězci, soubory, datovými strukturami a sítěmi. Dále je možné si vytvořit vlastní moduly a použít je v různých projektech. Moduly jsou načítány pomocí příkazu "import". Například pro načtení modulu pro práci s micro:bitem se použije následující:
```python
import microbit
# případně naimportujeme vše
from microbit import *
# nebo pouze konkrétní funkci foo pomocí
from microbit import foo 
```

## Obsah
[Button](#button)  
[Crash](#crash)  
[Distance](#distance) 
[Led](#led)   
[Matrix](#matrix)  
[Motor tbd](#motor)  
[Nezha tbd](#nezha)  
[Nixitube](#nixietube)  
[Servo tbd](#servo)  
[Trimpot tbd](#trimpot)  
[Další moduly](#more)  
## Button <a name="button"></a>
### Fyzická komponenta
[Button ElecFreaks doc](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05017.html)
### Dostupné metody
`C_is_pressed(self) -> bool`
  * Paramatery: None
  * Návratová hodnota:
    * True když je tlačítko C zmáčknuto, False jinak
  * Popis:
    * Slouží ke zjištění, zda je tlačítko C stisknuto či nikoliv.

`D_is_pressed(self) -> bool`
  * Paramatery: None
  * Návratová hodnota:
    * True když je tlačítko D zmáčknuto, False jinak
  * Popis:
    * Slouží ke zjištění, zda je tlačítko D stisknuto či nikoliv.

`CD_is_pressed(self) -> bool`
  * Paramatery: None
  * Návratová hodnota:
    * True když jsou obě tlačítka zmáčknuta, False jinak
  * Popis:
  * Slouží ke zjištění, zda jsou obě tlačítka stisknuto či nikoliv.

## Crash <a name="crash"></a>
### Fyzická komponenta
[Crash ElecFreaks doc](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05008.html)
### Dostupné metody
`crash_is_pressed(self) -> bool`
  * Paramatery: None
  * Návratová hodnota:
    * True když senzor zaznamenal náraz, False jinak
  * Popis:
    * Slouží ke zjištění, zda senzor zaznamenal náraz.

## Distance <a name="distance"></a>
### Fyzická komponenta
[Sonar:bit ElecFreaks doc](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05007.html)
### Popis
Modul Sonar:bit dokáže určit vzdálenost objektu pomocí ultrazvukového senzoru. Když signál narazí na objekt, odrazí se a putuje zpět k sonaru. Na základě doby návratu signálu je schopen určit přibližnou vzdálenost. 
### Použití
Může být použit k předběžnému posouzení podmínek na silnici, když ovládáte auto na dálku.
### Dostupné metody
`get_distance(self, unit=0) -> float`
  * Parametry: 
    * Optional[unit] (int), výchozí = 0 pro metrické (centimetry), 1 pro imperiální (palce)
  * Návratová hodnota: 
    * Vzdálenost (float)
  * Popis: Spočítá a vrátí vzdálenost od objektu

## Led <a name="led"></a>
### Fyzická komponenta
[Led ElecFreaks doc](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05009.html)
### Dostupné metody
`set_led(self, state: bool, brightness=100) -> None`
  * Parametry:
    * Stav (bool): True k zapnutí, False k vypnutí diody
    * Optional[brightness] (int): výchozí = 100, <0,100>, je-li stav 0. ignoruje se
  * Návratová hodnota: None
  * Výjimka `ValueError` při hodnotě brightness mimo rozsah
  * Popis: Rozsvěcí diodu, pokud je state True, zhasíná jinak.

`set_led_on(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Rozsvěcí diodu, vnitřně volá set_led(True, brightness=80)

`set_led_off(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Zhasíná diodu, vnitřně volá set_led(False)
  
`set_led_brightness(self, brightness) -> None`
  * Parametry:
    * brightness (int): jas
  * Návratová hodnota: None
  * Výjimka `ValueError` při hodnotě brightness mimo rozsah
  * Popis: Nastavuje jas diody, vnitřně volá set_led(True, brightness=brightness)
  
`get_is_on(self) -> bool`:
  * Parametry: None
  * Návratová hodnota: True, je-li didoa rozsvícena, False jinak
  * Popis: Slouží ke zjištění stavu diody.

`get_brightness(self) -> int`
  * Parametry: None
  * Návratová hodnota: 
    * brightness (int): hodnota jasu
  * Popis: Slouží ke zjištění jasu diody.

## Matrix<a name="matrix"></a>
### Fyzická komponenta
[8x16 Matrix Module in ElecFreaks doc](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05029.html)
### Popis
Modul 8 x 16 Matrix je druh maticové obrazovky 8 x 16, která dokáže zobrazovat čísla, běžně používaná písmena a symboly s rolovací funkcí.
### Použití
Dá se využít pro zobrazení konkrétních bodů v souřadnicovém systému.
### Dostupné metody
`def set_matrix_clear(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Zhasne všechny body matice

`set_matrix_draw(self, x: int, y: int) -> None`
  * Parametry:
    * Index souřadnice x (int) v intervalu 0-15,
    * Index souřadnice y (int) v intervalu 0-7
  * Návratová hodnota: None
  * Výjimka `ValueError` při hodnotě souřadnic mimo rozsah
  * Popis: Rozsvítí diodu na daných souřadnicích

`set_matrix_draw_position(self, position: int) -> None`
  * Parametry:
    * Pozice (int) v intervalu 0-128,
  * Návratová hodnota: None
  * Popis: Rozsvítí diodu na dané pozici dle řádků matice 

`set_matrix_expression(self, emoji: str) -> Nonew`
  * Parametry:
    * Name of emoji (str), platné hodnoty jsou: Neutral, Sad, Smile, Angry
  * Návratová hodnota: None
  * Výjimka `ValueError` při neznámé hodnotě emoji
  * Popis: Rozsvítí diody a vytvoří obraz zadaného emoji 

## Motor <a name="motor"></a>
### Fyzická komponenta

### Popis
Třída `Motor` není standardní součástí balíčku modulů výrobce. Pro usnadnění práce s ním byla původní třída Nezha rozdělena do dvou `Motor` a `Servo`.
Pozor na použití motoru. Při špatném zapojení motoru do soustavy pohonu se vám obrátí polarita a motor se točí obráceně.
### Dostupné metody
`set_motor(self, speed: int) -> None`
  * Parametry:
    * speed (int): rychlost v intervalu <-100, 100>
  * Návratová hodnota: None
  * Výjimka `ValueError` při hodnotě speed mimo rozsah
  * Popis: Nastaví rychlost motoru


## Nezha <a name="nezha"></a>
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


## Nixietube <a name="nixietube"></a>
### Fyzická komponenta
TODO
### Popis
TODO
### Použití
TODO
### Dostupné metody

## Servo <a name="servo"></a>
Třída `Servo` není standardní součástí balíčku modulů výrobce. Pro usnadnění práce s ním byla původní třída Nezha rozdělena do dvou `Motor` a `Servo`.
### Fyzická komponenta
. TODO

## Trimpot <a name="trimpot"></a>
### Fyzická komponenta
. TODO

## Další moduly <a name="more"></a>
Další moduly a jejich dokumentaci najdete v [dokumentaci eleckfreaks](https://www.elecfreaks.com/learn-en/microbitplanetX/index.html)
