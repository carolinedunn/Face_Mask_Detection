from gpiozero import Buzzer, LED
from time import sleep

buzzer = Buzzer(21)
red = LED(14)
green = LED(15)

while True:
    buzzer.on()
    green.off()
    red.on()
    sleep(1)
    buzzer.off()
    red.off()
    green.on()
    sleep(1)
