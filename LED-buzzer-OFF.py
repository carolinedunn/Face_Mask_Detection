#in case your LEDs or buzzer gets stuck in the on position
#   this turns LEDs and buzzer OFF

from gpiozero import Buzzer, LED
from time import sleep

buzzer = Buzzer(21)
red = LED(14)
green = LED(15)

buzzer.off()
red.off()
green.off()
sleep(1)
