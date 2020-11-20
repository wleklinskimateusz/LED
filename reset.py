from gpiozero import PWMLED

red = PWMLED(17)
green = PWMLED(22)
blue = PWMLED(24)

for col in [red, green, blue]:
    col.off()
