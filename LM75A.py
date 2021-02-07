#!/usr/bin/python

# Raspberry Pi LM75A I2C temperature sample code.

import sys
import smbus
import pyrebase
import time

config = {
  "apiKey": "AIzaSyDBeDtDn460CpLwkfpSMXWC1nclMAb-N4I",
  "authDomain": "lm75-4192f.firebaseapp.com",
  "databaseURL": "https://lm75-4192f-default-rtdb.firebaseio.com",
  "storageBucket": "lm75-4192f.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

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
  data={"temp":temperature}
  db.child("LM75").set(data)
  print ("{:.1f}C".format(temperature))
  time.sleep(5)
