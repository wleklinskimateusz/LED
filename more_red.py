from gpiozero import PWMLED

red = PWMLED(17)

if red.value <= 0.9:
    red.value += 0.1
