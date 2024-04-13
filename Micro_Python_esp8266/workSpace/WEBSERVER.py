import machine
import usocket as socket
import time
import network 

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('My_Station', 'myhome@123')
# Wait for connection
while True:
    if wifi.isconnected():
        print("Connected")
        print(wifi.ifconfig())
        break

print("Hello")

# HTML content for the web page
html = '''<!DOCTYPE html>
<html>
<center><h2>ESP8266 WEBSERVER</h2></center>
<form>
<center>
<h3>LED</h3>
<button name="LED" value='ON' type='submit'>ON</button>
<button name="LED" value='OFF' type='submit'>OFF</button>
</center>
'''

# Initialize LED pin
LED = machine.Pin(2, machine.Pin.OUT)
LED.value(0)  # Initially turn off the LED

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
Host = ''
Port = 80
s.bind((Host, Port))

# Listen for incoming connections
s.listen(5)

while True:
    # Accept incoming connection
    connection_socket, address = s.accept()
    print("Got a connection from", address)
    # Receive request from the client
    request = connection_socket.recv(1024)
    print("Content", request)
    request = str(request)
  
    # Find if the request contains '/?LED=ON' or '/?LED=OFF'
    LED_ON = request.find('/?LED=ON')
    LED_OFF = request.find('/?LED=OFF')
  
    # Toggle LED based on the request
    if LED_ON == 6:
        LED.value(0)  # Turn on the LED
    elif LED_OFF == 6:
        LED.value(1)  # Turn off the LED

    # Send the HTML response
    response = html
    connection_socket.send(response)
    # Close the connection
    connection_socket.close()

