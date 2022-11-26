from machine import PWM, Pin
from time import sleep
from random import randint

green = Pin(25, Pin.OUT)
buzz = PWM(Pin(16))
vol = 1000
Pin1 = PWM(Pin(15))
n=0.5
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
        note(int(G), vol, 1.5 )
     
  
    
    
    

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
    
   if n<3.5:
       song()
       n = n + 0.5
   else:
       n = 0.5

