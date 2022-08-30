#!/usr/bin/env python3
import requests
import binascii
import config
 
def send_info_pump(moisture_to_add):
  """
    Send the moisture to our microcontroller (through the Frost sever) the number of milliseconds of pumping for the plant
    Return 0 if success, else return the response
    ---------------------
    parameters:
    moisture_to_add: float
        moisture we want to add to the plant (in percent)
    """

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
  
  # convert moisture in percent to milliseconds of pumping
  time_second = moisture_to_add *(1000/config.conversion_moisture_volume)*(1/config.flow_rate_pump)
   # Set values (converted in u_int8) to array positions
  arr[0] = int((time_second/20)*255)

  # Convert bytearray to UTF-8 HEX String
  hex = binascii.hexlify(bytearray(arr))
  hex_string = hex.decode('utf-8')
  
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

if __name__ == "__main__":

  # For testing purposes

  moisture_to_add = 5
  send_info_pump(moisture_to_add)