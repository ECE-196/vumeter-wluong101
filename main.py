# Write your code here :-)
import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    print(volume)

    #leds[0].value = not leds[0].value
    #leds[1].value = not leds[0].value
    #sleep(1)

    x = 0
    for x in range(0,11):
        if volume > 23000 + (x * 2600):
            leds[x].value = 1
        else:
            leds[x].value = 0

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
