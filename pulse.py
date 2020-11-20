from gpiozero import PWMLED
from time import sleep
from random import randint

red = PWMLED(17)
green = PWMLED(22)
blue = PWMLED(24)

while True:
    red.pulse()
    sleep(1.3)

    green.pulse()
    sleep(3.2)

    blue.pulse()
    sleep(6)
