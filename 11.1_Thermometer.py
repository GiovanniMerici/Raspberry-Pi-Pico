from machine import Pin, ADC, PWM
import time
import math

#Set ADC
adc=ADC(26)
led = Pin(25, Pin.OUT)
pwm = PWM(Pin(15))
pwm.freq(10000)
Buzz = PWM(Pin(16))
Buzz.freq(10000)
try:
    while True:
        adcValue = adc.read_u16()
        val = 0
        led.value(val)
        Buzz.duty_u16(adcValue)
        voltage = adcValue / 65535.0 * 3.3
        Rt = 10 * voltage / (3.3-voltage)
        tempK = (1 / (1 / (273.15+25) + (math.log(Rt/10)) / 3950))
        tempC = int(tempK - 273.15)
        tempL = 2 ** int(tempC / 2)
        Buzz.duty_u16(tempL)
        pwm.duty_u16(tempL)
        print("ADC value:", adcValue, "  Voltage: %0.2f"%voltage,
              "  Temperature: " + str(tempC) + "C")
        time.sleep(1)
        val = 1
        led.value(val)
        
except:
    pass