#imports
import RPi.GPIO as GPIO
import pyrebase
import time
import requests
import json

sensor = 40
buzzer = 23
LED = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(LED,GPIO.OUT)

GPIO.output(buzzer,False)
print("IR Sensor Ready ...")
print(" ")
try:
    while True:
      if GPIO.input(sensor):
       GPIO.output(LED,True)
       print("Object Detected")
       
       url = "https://us-central1-personify-c98fc.cloudfunctions.net/postDeviceData"
       data = {
        "uid": "XHVfPr23F7Meg0QuwEkYFvI8Fqd2",
        "accessCode": "apple",
        "DATA": {
        "value": True,
        "type": "IR"
                  }
                }
       headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
       r = requests.post(url, data=json.dumps(data), headers=headers)

       time.sleep(2)
      else:
       url = "https://us-central1-personify-c98fc.cloudfunctions.net/postDeviceData"
       data = {
       		"uid": "XHVfPr23F7Meg0QuwEkYFvI8Fqd2",
       		 "accessCode": "apple",
       		"DATA": {
       		 "value": False,
       		 "type": "IR"
          		 }
   		 }
       headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
       r = requests.post(url, data=json.dumps(data), headers=headers)


       GPIO.output(LED,False)
       print("none")
       time.sleep(2)

except KeyboardInterrupt:
       GPIO.cleanup()
