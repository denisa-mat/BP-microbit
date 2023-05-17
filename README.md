# Moduly
V Pythonu jsou moduly soubory, které obsahují definice funkcí, tříd a proměnných, které lze použít v jiných programech. Moduly jsou používány pro organizaci kódu do logických bloků a pro znovupoužitelnost kódu.

Python má mnoho vestavěných modulů, jako jsou moduly pro práci s řetězci, soubory, datovými strukturami a sítěmi. Dále je možné si vytvořit vlastní moduly a použít je v různých projektech. Moduly jsou načítány pomocí příkazu `import`. Například pro načtení modulu pro práci s micro:bitem se použije následující:
```python
import microbit
# případně naimportujeme vše
from microbit import *
# nebo pouze konkrétní funkci foo pomocí
from microbit import foo 
```
:warning: Většina modulů je upravena pro potřeby tohoto kurzu. Funkcionalita byla přidávána, neubírána, ale plná zpětná kompatibilita přesto není zaručena. Některé metody se chovají trochu jinak, například přibyly výjimky pro nevalidní vstupy.

:warning: Moduly byly oproti verzi dodané výrobcem v mnohém vylepšeny, ale stále nejsou dokonalé a nějakou úpravu by si jistě zaloužily.
## Obsah
[Button](#button)  
[Crash](#crash)  
[Distance](#distance) 
[Led](#led)   
[Matrix](#matrix)  
[Motor](#motor)  
[Nezha](#nezha)  
[Nixitube](#nixietube)  
[Servo](#servo)  
[Trimpot](#trimpot)  
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
### Popis
:warning: Třída `Motor` není standardní součástí balíčku modulů výrobce. Pro usnadnění práce s ním byla původní třída Nezha rozdělena do dvou `Motor` a `Servo`.

:warning: Pozor na použití motoru. Při špatném zapojení motoru do soustavy pohonu se vám obrátí polarita a motor se točí obráceně.
### Dostupné metody
`set_motor(self, speed: int) -> None`
  * Parametry:
    * speed (int): rychlost v intervalu <-100, 100>
  * Návratová hodnota: None
  * Výjimka `ValueError` při hodnotě speed mimo rozsah
  * Popis: Nastaví rychlost motoru

`set_motor_forward_slow(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Nastaví rychlost motoru na pomalu, vnitřně volá set_motor(20).

`set_motor_forward_fast(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Nastaví rychlost motoru na rychle, vnitřně volá set_motor(60).

`set_motor_forward_very_fast(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Nastaví rychlost motoru na velmi rychle, vnitřně volá set_motor(100).

`set_motor_stop(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Zastaví motor, vnitřně volá set_motor(0).

`set_motor_backward_slow(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Nastaví rychlost motoru na zpátky pomalu, vnitřně volá set_motor(-20).

`set_motor_backward_fast(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Nastaví rychlost motoru na zpátky rychle, vnitřně volá set_motor(-60).

`set_motor_backward_very_fast(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Nastaví rychlost motoru na zpátky velmi rychle, vnitřně volá set_motor(-100).

`get_motor_speed(self) -> int`
  * Parametry: None
  * Návratová hodnota:
    * speed (int): rychlost, v rozsahu <-100, 100>
  * Popis: Slouží ke zjištění rychlosti.

`get_motor_goes_forward(self) -> bool`
  * Parametry: None
  * Návratová hodnota:
    * goes_forward (bool): True pokud motor jede vpřed, False jinak
  * Popis: Slouží ke zjištění, zda motor jede vpřed. Pro zjištění, zda couvá, použijte metodu `get_motor_speed`
  
## Nezha <a name="nezha"></a>
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
  * Popis: Nastavuje úhel serva

## Nixietube <a name="nixietube"></a>
### Fyzická komponenta
[7-Seg LED Nixietube in ElecFreaks doc](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05026.html)
### Popis
Jde o sedmisegmentový displej, primárně pro zobrazování čísel.
### Použití
Sensor je schopen zobrazit čas, skóre nebo jiné číselné údaje.
### Dostupné metody
`set_power_on(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Rozsvěcí celý displej

`set_power_off(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Zhasíná celý displej

`set_intensity(self, intensity) -> None`
  * Parametry:
    * intensity (int): intenzita v rozmezí <0, 8>
  * Návratová hodnota: None
  * Popis: Nastavuje intenzitu svícení displeje
  
`set_clear(self) -> None`
  * Parametry: None
  * Návratová hodnota: None
  * Popis: Resetuje hodnoty na displeji

`set_show_bit(self, num: int, bit=0) -> None`
  * Parametry:
    * num (int): číslo k zobrazení v rozmezí <0, 9>
    * Optional[bit] (int): pozice, na kterém se má číslo zobrazit, default = 0, v rozmezí <0, 3>
  * Návratová hodnota: None
  * Popis: Zobrazuje číslo z parametru num na displeji. Lze specifikovat pozici užitím paramteru bit

`set_show_num(self, num: int) -> None`
  * Parametry:
    * num (int): number to be shown, valid within <-999, 9999>
  * Návratová hodnota: None
  * Popis: Zobrazuje číslo num na displeji. Číslice na bitech, které se na displej nevejdou, se zahazují

## Servo <a name="servo"></a>
:warning: Třída `Servo` není standardní součástí balíčku modulů výrobce. Pro usnadnění práce s ním byla původní třída Nezha rozdělena do dvou `Motor` a `Servo`.
### Dostupné metody
`set_servo(self, angle)`
  * Parametry:
    * Konektor (int), do kterého je připojeno servo v intervalu 1-4
    * Úhel (int) nákolu v intervalu 0-180
  * Návratová hodnota: None
  * Výjimka: `ValueError('angle error,0~180')` upozorňuje na hodnotu mimo validní rozsah
  * Popis: Nastavuje úhel serva.

## Trimpot <a name="trimpot"></a>
### Dostupné metody
`get_trimpot_value(self)`
  * Parametry: None
  * Návratová hodnota:
    * value (float): hodnota naměřené odporu v intervalu <0, 1023>
  * Popis: Vrací hodnotu naměřeného odporu v intervalu <0, 1023>

## Další moduly <a name="more"></a>
Další moduly a jejich dokumentaci najdete v [dokumentaci eleckfreaks](https://www.elecfreaks.com/learn-en/microbitplanetX/index.html).
