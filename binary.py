#GPIO port for each LED from left to right: 26 19 13 21 20 22 27 17
from gpiozero import LED

LEDS = [LED(17),LED(27),LED(22),LED(20),LED(21),LED(13),LED(19),LED(26)]

def num_to_binary(n):
    if n == 1:
        return "1"
    elif n%2 == 1:
        return "1" + num_to_binary((n-1)/2)
    else:
        return "0" + num_to_binary((n)/2)

binary = num_to_binary(int(input("What number? ")))

while True:
    for n in range(len(binary)):
        if binary[n] == "1":
            LEDS[n].on()
        else:
            LEDS[n].off()