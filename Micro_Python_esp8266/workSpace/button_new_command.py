from machine import Timer ,Pin

led = Pin(2,Pin.OUT)
but = Pin(0,Pin.IN)

def button_irq(pin):
  print("Triggered")

timer = Timer(0)
timer.init(period = 1000,mode=Timer.PERIODIC ,callback = lambda t: led.value(not led.value()))

but.irq(trigger=Pin.IRQ_FALLING, handler=button_irq)
