from machine import Pin, PWM
from random import randint
import time

pins = [13, 12, 11]
freq_num = 100

led1 = Pin(pins[0], Pin.OUT)
led2 = Pin(pins[1], Pin.OUT)
led3 = Pin(pins[2], Pin.OUT)


    
while True:
    val1 = randint(0,1)
    val2 = randint(0,1)
    val3 = randint(0,1)
    time.sleep_ms(2)
    led1.value(val1)
    led2.value(val2)
    led3.value(val3)
    