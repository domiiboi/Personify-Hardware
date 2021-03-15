IR Proximity sensor has IR LED as IR transmitter and Photo diode as IR detector. 
The control circuit consists of Op-amp IC LM358 and associated components such as Four 220ohm resistors, 10K ohm resistor, 10k ohm potentiometer and RED LED.

Python code below has integrated IR proximity sensor having RPI with Pyrebase and firebase DB. 
The code imports Library for GPIO and Pyrebase. Firebase configuration is given with apiKey, authDomain, databaseURL and storageBucket. 
While loop runs repeatedly and activates the buzzer to give sound when the object is detected by the IR sensor. (here object is person's hand). 
Then, data proximity is set to 1, so the child proximity set to 1 for firebase. There is sleep time involved for 2sec.

Note: IF statement checking IR sensor was not added as it may not be required since IR sensor is connected to RPI on PCB when it is being used. 
Also, the second while loop for GPIO.input(sensor) may not be required as GPIO.input(sensor) is already passed by while true loop, 
i.e sensor is checked already and displaying as object detected when there is a person's hand. 
If we place a second while loop with GPIO.input(sensor), it must be false in order to introduce time delay, 
but as GPIO.input(sensor) has to be true when object is detected so to introduce time delay for each object detected message, it's better to remove second while loop. 


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
  "apiKey": " ",
  "authDomain": "lm75-4192f.firebaseapp.com",
  "databaseURL": "https://lm75-4192f-default-rtdb.firebaseio.com",
  "storageBucket": "lm75-4192f.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

try: 
   while True:
          GPIO.input(sensor):
          GPIO.output(buzzer,True)
          print "Object Detected"
	  data={"proximity":1}
  	  db.child("PIR").set(data)
          time.sleep(2)
      

except KeyboardInterrupt:
    GPIO.cleanup()

