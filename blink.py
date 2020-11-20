from gpiozero import PWMLED
from time import sleep

red = PWMLED(17)
green = PWMLED(22)
blue = PWMLED(24)
red.value = 0
green.value = 0
i = 0

# while True:
#     for i in range(100):
#         #red.value = i/100
#         blue.value = i/100
#         #green.value = i/100
#         sleep(0.1)
