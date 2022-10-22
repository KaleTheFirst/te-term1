from gpiozero import LED
from time import sleep

led = LED(17) 

while True:
    first = input("")
    if first == "on":
        led.on()
    elif first == "off":
        led.off()
    else:
        print("try again")