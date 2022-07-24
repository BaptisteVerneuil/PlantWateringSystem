#!/usr/bin/env python3
import requests
import binascii
 
def send_info_pump(moisture_to_add):
  # SWM LoRaWAN config ----------------------------------------------------------
  url = 'https://iot-lns.swm.de/1/rest'
  token = 'Bearer vgEAGAAAAA5pb3QtbG5zLnN3bS5kZbtqvQH--h5qpruoSK4aJBo='
  
  eui = '00B193384D6E47B8'
  port = 33
  confirmed = 'false'
  appid = 'BE01000A'
  
  # LoRaWAN payload -------------------------------------------------------------
  size = 1                    # Length of the byte array
  arr = bytearray(size)       # Init byte array
  
  # Set values (u_int8) to array positions
  arr[0] = int((moisture_to_add/100)*255)
  # print(arr)

  # Convert bytearray to UTF-8 HEX String
  hex = binascii.hexlify(bytearray(arr))
  hex_string = hex.decode('utf-8')
  # print(hex)
  # print(hex_string)
  
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
    return 0
  else:
    return [response.status_code, response.reason]