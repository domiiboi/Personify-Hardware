from apds9960.const import *
from apds9960 import APDS9960
import RPi.GPIO as GPIO
import smbus
from time import sleep
import pyrebase

config = {
  "apiKey": " ",
  "authDomain": " ",
  "databaseURL":"https://firstpy-b9b91-default-rtdb.firebaseio.com",
  "storageBucket": " "
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
info = db.child("data").child("light").get()

port = 1
bus = smbus.SMBus(port)
apds = APDS9960(bus)


try:
    print("Light Sensor")
    print("============")
    apds.enableLightSensor()    
    oval = -1
    
    while True:
        sleep(1)
        val = apds.readAmbientLight()
        if val != oval:
		print("Light Detected={}".format(val))
        db.child("data").update({"light":val})
        oval = val
finally:
    GPIO.cleanup()
    print("Bye")
