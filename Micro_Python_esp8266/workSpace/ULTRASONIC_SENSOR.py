from machine import Pin
from time import sleep,ticks_us, ticks_diff
 
ECHO = Pin(14,Pin.IN)
TRIG = Pin(12,Pin.OUT)
  
  
def measure():
    TRIG.value(0)
    sleep(0.2)
    TRIG.value(1)
    sleep(0.2)
    TRIG.value(0)
    
    pulse_start = 0
    pulse_end = 0
    
    while ECHO.value() == 0:
      pulse_start = ticks_us()

    # Wait for echo pin to go low
    
    while ECHO.value() == 1:
      pulse_end = ticks_us()

    # Calculate pulse duration in microseconds
    pulse_duration = ticks_diff(pulse_end, pulse_start)

    # Speed of sound in air is approximately 343 meters per second or 0.0343 cm/µs
    # Distance = (pulse duration * speed of sound) / 2
    distance = (pulse_duration * 0.0343) / 2

    return distance
  
while True:
   
   distance = measure()
   print("Distance:", distance, "cm")
   sleep(1)
   

  
