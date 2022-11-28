from machine import PWM, Pin
from time import sleep
from random import randint

button = Pin(18, Pin.IN, Pin.PULL_UP)
green = Pin(25, Pin.OUT)
buzz = PWM(Pin(16))
vol = 1000
Pin1 = PWM(Pin(15))
n = 0.5
b = 0
blue = PWM(Pin(13))
red = PWM(Pin(12))
green1 = PWM(Pin(11))
def note(frequency,vol,time):
   # vol = randint(0,10335) drunk jingleBells
    buzz.freq(int(frequency*n))
    buzz.duty_u16(vol)
    if vol != 0:
        Pin1.duty_u16(2 ** int(frequency / 50) )
        green.value(0)
    else:
        Pin1.duty_u16(0)
        green.value(1)
    sleep(time)

def song():
        for i in range(0,2):
            note(int(E), vol, 0.35)
            note(int(E), 0, 0.1)
            note(int(E), vol, 0.35)
            note(int(E), 0, 0.1)
            note(int(E), vol, 0.35 )
            note(int(E), 0, 0.1)
    
            note(int(E), 0, 0.4)
    
      
        note(int(E), vol, 0.5 )
        note(int(G), vol, 0.5 )
        note(int(C), vol, 0.5 )
        note(int(D), vol, 0.5 )
        note(int(E), vol,1.5 )

        note(int(F), vol, 0.35)
        note(int(F), 0, 0.1)
        note(int(F), vol, 0.35)
        note(int(F), 0, 0.1)
        note(int(F), vol, 0.35 )
        note(int(F), 0, 0.1)
        note(int(F), vol, 0.35 )
        note(int(F), 0, 0.1)

        note(int(F), vol, 0.35)
        note(int(F), 0, 0.1)
        note(int(E), vol, 0.35)
        note(int(F), 0, 0.1)
        note(int(E), vol, 0.35 )
        note(int(F), 0, 0.1)       

        note(int(E), vol, 0.35)
        note(int(F), 0, 0.1)
        note(int(D), vol, 0.35)
        note(int(F), 0, 0.1)
        note(int(D), vol, 0.35 )
        note(int(F), 0, 0.1)
        note(int(E), vol, 0.35)
        note(int(F), 0, 0.1)
        note(int(D), vol, 0.35)
        note(int(F), 0, 0.1)
        note(int(G), vol, 1.2 )

def Bee():   
    for x in (0,2):
        note(int(G), vol, 0.2 )
        note(int(G), vol, 0.2 )
        note(int(G), vol, 0.2 )
        note(int(Ef), vol, 0.7 )
        note(int(F), vol, 0.2 )
        note(int(F), vol, 0.2 )
        note(int(F), vol, 0.2 )
        note(int(D), vol, 0.7 )
    for x in (0,2):
        note(int(G), vol, 0.1 )
        note(int(G), vol, 0.1 )
        note(int(G), vol, 0.1 )
        note(int(Ef), vol, 0.6 )
        note(int(F), vol, 0.1 )
        note(int(F), vol, 0.1 )
        note(int(F), vol, 0.1 )
        note(int(D), vol, 0.6 )
    
    
def butt():
    if not button.value():
        b = 1
        print(b)
        sleep(0.3)
        if not button.value():
            b = 2
            print(b)
            green.value(1)
            Bee()
            
        if b == 1:
            green1.duty_u16(65335)
            red.duty_u16(65335)
            blue.duty_u16(65335)
            song()
        sleep(0.1)
    else:
        b = 0
        print(b)
        green1.duty_u16(int(randint(0,65335)))
        blue.duty_u16(int(randint(0,65335)))
        red.duty_u16(int(randint(0,65335)))
        sleep(0.1)
        buzz.duty_u16(0)
        Pin1.duty_u16(0)

Pin1.duty_u16(0)  
N= 0
A = 440
Af = 466.16
B = 493.88
C = 523.25
D = 587.33
E = 659.25
F = 698.46
G = 783.99
Ef = 622.25
Df= 554.37
Gf = 739.99
G4= 392.00


notes =[440, 493.88, 523.25, 587.33, 659.25, 698.46, 783.99] 
    
while True:
    butt()