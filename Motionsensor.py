from machine import Pin, PWM
import utime

buzz = PWM(Pin(15))
buzz.freq(50)
red = Pin(13, Pin.OUT)
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
led = Pin(25, Pin.OUT)
global t, diff, distance
distance = 0
t = 0
diff = 0

def ultra():
   
   global t, diff, distance
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff

   distance = (timepassed * 0.0343) / 2
   diff = (t - distance) ** 2
   t = distance
   print('difference is: ',diff)
   if distance<200:
       if diff<30:
           led.value(1)
           buzz.duty_u16(0)
           red.value(0)
           
       else:
           led.value(0)
           buzz.duty_u16(5000)
           red.value(1)
           print('DANGER')
           utime.sleep(0.5)
   else:
        led.value(1)
        buzz.duty_u16(0)
        red.value(0)
        
   print("The distance from object is ",distance,"cm")

while True:
   ultra()
   utime.sleep(1)