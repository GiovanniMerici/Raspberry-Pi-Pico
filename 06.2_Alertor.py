from machine import Pin,PWM
import math
import time
PI = 3.14
b = 0
button = Pin(16, Pin.IN, Pin.PULL_UP)
passiveBuzzer = PWM(Pin(15))
passiveBuzzer.freq(1000)
pwm = PWM(Pin(14))
pwm.freq(1000)
led = Pin(25, Pin.OUT)

def alert():
    for x in range(0, 36):
        sinVal  = math.sin(x * 10 * PI / 180)
        toneVal = 1500+int(sinVal*500)
        passiveBuzzer.freq(toneVal)
        pwm.duty_u16(toneVal*3^x)
        time.sleep_ms(100)


try:
    while True:
        if not button.value():
            b = b + 1
            print(b+10)
            while b == 1:
                passiveBuzzer.duty_u16(4092*2)
                pwm.duty_u16(10)
                led.value(1)
                alert()
                
                time.sleep(1)
                if  button.value():
                    print(b)
                else:
                    b = 0 
                    print(b)
                time.sleep(2)
        else:
            passiveBuzzer.duty_u16(0)
            pwm.duty_u16(0)
            led.value(0)
            
     
            
except:
        passiveBuzzer.deinit()
        