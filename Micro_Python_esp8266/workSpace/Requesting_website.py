import network 
import urequests

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect('My_Station','myhome@123')
#wifi.connect('AndroidAP','198643harshal')

while True:
    if(wifi.isconnected()== True):
     print("connected")
     print(wifi.ifconfig())
     break

req = urequests.get('https://www.example.com')
print(req.status_code)
print(req.text)
