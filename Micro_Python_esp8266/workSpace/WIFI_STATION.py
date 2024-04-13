import network 

wifi = network.WLAN(network.AP_IF)
wifi.active(True)

wifi.config(essid = 'ESP_STATION',password = 'ESP_8266',authmode=network.AUTH_WPA_PSK )

print(wifi.ifconfig())
print(wifi.isconnected())

while True:
    if(wifi.isconnected()== True):
     print("connected")
     break
