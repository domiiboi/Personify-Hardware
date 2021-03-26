from apds9960.const import *
from apds9960 import APDS9960
import smbus
from time import sleep
import pyrebase
import requests,json


url = 'https://us-central1-personify-c98fc.cloudfunctions.net/postDeviceData'




config = {
  "apiKey": " ",
  "authDomain": " ",
  "databaseURL":"https://firstpy-b9b91-default-rtdb.firebaseio.com",
  "storageBucket": " "
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

port = 1
bus = smbus.SMBus(port)
apds = APDS9960(bus)

try:
 print("Light Sensor")
 print("============")
 apds.enableLightSensor()
 oval = -1

 while True:
  sleep(10)
  val = apds.readAmbientLight()
  if val != oval:
   print("Light Detected={}".format(val))


   data= {"uid":'XHVfPr23F7Meg0QuwEkYFvI8Fqd2',"accessCode":"apple",
          "DATA":{'value':val,'type':"LIGHT_SENSOR"}
         }
   headers = {'Content-type':'application/json','Accept':'text/plain'}

   x = requests.post(url, data=json.dumps(data), headers=headers)

   print(x.text)


   db.child("data").update({"light":val})
   oval = val
finally:
    print("Bye")
    apds.disableLightSensor()

