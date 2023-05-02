# Lekce 5
### Seznamy, indexace, foreach

## Obsah
[Motivace](#motivace)  
[Prostředky I - Seznam, indexace ](#resources1)  
[Úloha 1 - ](#assignment1)  
[Prostředky II - ](#resources2)  
[Úloha 2 - ](#assignment2)  
[Úloha 3 - ](#assignment3)  
[Shrnutí](#conclusion)  
[Poznámky pro učitele](#pozn)  

## Motivace <a name="motivace"/>
TODO
## Prostředky I - <a name="resources1"/>
## Úloha 1 - Proměnné <a name="assignment1"/>
### Zadání
TODO
### Co budete potřebovat
TODO
### Co se naučíte
TODO
### Vzorová implementace
```python
from microbit import *
from button import *

button = BUTTON(J1)

list = ["C", "D", "D", "C", "C"]
input = []

for value in list:
    display.scroll(value)

C_was_pressed = False
D_was_pressed = False
all_correct = True

for i in list:
    while not C_was_pressed and not D_was_pressed:
        C_was_pressed = button.C_is_pressed()
        D_was_pressed = button.D_is_pressed()
    if (C_was_pressed and i != "C") or (D_was_pressed and i != "D"):
        display.show(Image.NO)
        all_correct = False
    sleep(300)
    C_was_pressed = False
    D_was_pressed = False
    display.clear()
if all_correct:
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)
```

### Popis řešení
TODO
### Doplňující poznámky 
TODO
## Prostředky II -  <a name="resources2"/>
TODO
## Úloha 2 - <a name="assignment3"/>
### Zadání
TODO
### Co budete potřebovat
TODO
### Co se naučíte
TODO
### Vzorová implementace

```python
from microbit import *
from button import *
from led import *

button = BUTTON(J1)
green_led = LED(J2)
red_led = LED(J3)

int_values = []

for i in range(0, 6):
    int_values.append(random.randint(0,2))

button_values = []

for i in range(len(values)):
    if int_values[i] = 0:
	button_values[i] = "C"
    else:
	button_values[i] = "D"

for value in list:
    display.scroll(value)

input = []
C_was_pressed = False
D_was_pressed = False

for i in range(len(list)):
    while not C_was_pressed and not D_was_pressed:
        C_was_pressed = button.C_is_pressed()
        D_was_pressed = button.D_is_pressed()
        
    if C_was_pressed: 
        input.append("C")
    elif D_was_pressed:
        input.append("D")
        
    if list[i] == input[i]:
        green_led.set_led_on()
    else:
        red_led.set_led_on()
    sleep(600)
    C_was_pressed = False
    D_was_pressed = False

    red_led.set_led_off()
    green_led.set_led_off()
    
if list == input:
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)
```

### Popis řešení
TODO
### Doplňující poznámky 
TODO
## Shrnutí <a name="conclusion"/>
TODO
## Poznámky pro učitele <a name="pozn"/>
TODO

