from gpiozero import RGBLED
from time import sleep
from datetime import datetime, timedelta

led = RGBLED(red=17, green=22, blue=24)

today = datetime.now().day
i = 1
intensity = 1

while True:
    now = datetime.now()
    # print(now)
    if today != now.day:
        i = 0
        today = now.day



    check0 = datetime(now.year, now.month, now.day, 8, 0, 0)
    check1 = datetime(now.year, now.month, now.day, 11, 20, 0)
    check2 = datetime(now.year, now.month, now.day, 14, 40, 0)
    check3 = datetime(now.year, now.month, now.day, 18, 0, 0)
    check4 = datetime(now.year, now.month, now.day, 21, 20, 0)
    check5 = datetime(now.year, now.month, now.day + i, 0, 40, 0)
    check6 = datetime(now.year, now.month, now.day + i, 4, 0, 0)
    # print(check6)
    if today != now.day:
        today = now.day

    if now > check0 and now < check1:
        i = 1
        led.color = (intensity * abs((now - check1).seconds) / (check1 - check0).seconds, 0, intensity)

    if now > check1 and now < check2:
        led.color = (0, intensity * abs((now - check1).seconds) / (check1 - check0).seconds, intensity)

    if now > check2 and now < check3:
        led.color = (0, intensity, intensity * abs((now - check3).seconds) / (check1 - check0).seconds)

    if now > check3 and now < check4:
        led.color = (intensity * abs((now - check3).seconds) / (check1 - check0).seconds, intensity, 0)

    if now > check4 and now < check5:
        led.color = (intensity, intensity * abs((now - check5).seconds) / (check1 - check0).seconds, 0)

    if now > check5 and now < check6:
        led.color = (intensity, 0, intensity * abs((now - check5).seconds) / (check1 - check0).seconds)

    if now > check6 and now < check0:
        led.color = (0, 0, 0)

    # print(now > check5)
