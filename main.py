# main.py -- put your code here!
from machine import Pin
from neopixel import NeoPixel
import time

pin = Pin(48, Pin.OUT)   
neo = NeoPixel(pin, 1)   

while True:
    neo[0] = (0, 255, 0)  
    neo.write()           
    time.sleep(1)
    
    neo[0] = (255, 0, 0)  
    neo.write()           
    time.sleep(2)      
    
    neo[0] = (0, 0, 255) 
    neo.write()           
    time.sleep(2)