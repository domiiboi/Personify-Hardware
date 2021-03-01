import RPi.GPIO as GPIO
import time
import sys
import smbus
import pyrebase

sensor = 16
buzzer = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print "IR Sensor Ready....."
print " "
config = {
  "apiKey": "AIzaSyDBeDtDn460CpLwkfpSMXWC1nclMAb-N4I",
  "authDomain": "lm75-4192f.firebaseapp.com",
  "databaseURL": "https://lm75-4192f-default-rtdb.firebaseio.com",
  "storageBucket": "lm75-4192f.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,True)
          print "Object Detected"
		data={"proximity":1}
  		db.child("PIR").set(data)
          while GPIO.input(sensor):
              time.sleep(10)
      else:
          GPIO.output(buzzer,False)
		data={"proximity":0}
  		db.child("PIR").set(data)


except KeyboardInterrupt:
    GPIO.cleanup()