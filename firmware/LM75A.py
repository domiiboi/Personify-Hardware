#!/usr/bin/python

# Raspberry Pi LM75A I2C temperature sample code.

import sys
import smbus
import time

# By default the address of LM75A is set to 0x48
# aka A0, A1, and A2 are set to GND (0v).
address = 0x48

# Check if another address has been specified
if 1 < len(sys.argv):
	address = int(sys.argv[1], 16)

# Print temperature
while True:	

# Read I2C data and calculate temperature
  bus = smbus.SMBus(1)
  raw = bus.read_word_data(address, 0) & 0xFFFF
  raw = ((raw << 8) & 0xFF00) + (raw >> 8)
  temperature = (raw / 32.0) / 8.0
  
  #Push Data
 url = "https://us-central1-personify-c98fc.cloudfunctions.net/postDeviceData"
    data = {
    "uid": "XHVfPr23F7Meg0QuwEkYFvI8Fqd2",
    "accessCode": "apple",
    "DATA": {
        "value": temperature,
        "type": "TEMP"
      }
  }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.text)
  print ("{:.1f}C".format(temperature))
 
