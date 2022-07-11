#!/usr/bin/env python3
import requests
import binascii
 
# SWM LoRaWAN config ----------------------------------------------------------
url = 'https://iot-lns.swm.de/1/rest'
token = 'Bearer vgEAGAAAAA5pb3QtbG5zLnN3bS5kZbtqvQH--h5qpruoSK4aJBo='
 
eui = '00B193384D6E47B8'
port = 33
confirmed = 'false'
appid = 'BE01000A'
 
# LoRaWAN payload -------------------------------------------------------------
size = 3                    # Length of the byte array
arr = bytearray(size)       # Init byte array
 
# Set values (u_int8) to array positions
arr[0] = 1
arr[1] = 2
arr[2] = 255
print(arr)

# Convert bytearray to UTF-8 HEX String
hex = binascii.hexlify(bytearray(arr))
hex_string = hex.decode('utf-8')
print(hex)
print(hex_string)
 
# Build HTTP header
headers = {
    'Authorization': token,
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/json',
}
 
# Build HTTP body
data = '{\n"cmd": "tx",\n"EUI": "' + eui + '",\n"port": ' + str(port) + ',\n"confirmed": '+ confirmed + ',\n"data": "' + hex_string +  '",\n"appid": "' + appid + '"\n}'
 
# Send HTTP POST
response = requests.post(url, headers=headers, data=data)
 
# Check request response for errors
if response.status_code < 300:
  print('\nThat worked! HTTP Status: %s: %s' % (response.status_code, response.reason))
else:
  print('\nSometing went wrong: HTTP Status: %s: %s' % (response.status_code, response.reason))
  print('Check this for more: https://de.wikipedia.org/wiki/HTTP-Statuscode')