from machine import Pin, ADC, PWM
import time

adc = ADC(26)
adc1 = ADC(27)
pwm = PWM(Pin(15))
pwm1 = PWM(Pin(0))
pwm2 = PWM(Pin(8))
pwm.freq(10000)
pwm1.freq(10000)
pwm2.freq(10000)
try:
    while True:
        read = adc.read_u16()
        read1 = adc1.read_u16()
        pwm.duty_u16(read)
        pwm1.duty_u16(read)
        pwm2.duty_u16(read1)
        
        time.sleep(0.1)
except:
    pwm.deinit()