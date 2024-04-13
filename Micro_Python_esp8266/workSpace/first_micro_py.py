from machine import Pin 
from time import sleep

led = Pin(4,Pin.OUT)

while True:
  
  led.value(1)
  print("Led on")
  sleep(2)
  led.value(0)
  print("Led off")
  sleep(2)
