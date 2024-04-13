import network 

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect('My_Station','myhome@123')
#wifi.connect('AndroidAP','198643harshal')

while True:
    if wifi.isconnected():
     print("connected")
     print(wifi.ifconfig())
     break

print("hello")
