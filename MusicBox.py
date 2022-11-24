from machine import PWM, Pin
from time import sleep

buzz = PWM(Pin(16))
vol = 1500
Pin1 = PWM(Pin(15))
def note(frequency,vol,time):
    buzz.freq(frequency)
    buzz.duty_u16(vol)
    Pin1.duty_u16(2 ** int(frequency / 50) )
    sleep(time)

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


t=0.2
notes =[440, 493.88, 523.25, 587.33, 659.25, 698.46, 783.99] 
while True: 
    for i in notes:
        note(int(i), vol, t)
    for i in reversed(notes):
        note(int(i), vol, t )
    
    sleep(2)
    for x in (0,2):
        note(int(G), vol, 0.4 )
       
        note(int(G), vol, 0.4 )
     
        note(int(G), vol, 0.4 )
       
        note(int(Ef), vol, 1 )
       
        note(int(F), vol, 0.4 )
       
        note(int(F), vol, 0.4 )
    
        note(int(F), vol, 0.4 )
       
        note(int(D), vol, 1 )
       
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
        

     
   