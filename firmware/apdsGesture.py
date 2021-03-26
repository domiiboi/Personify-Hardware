from time import sleep
from apds9960.const import *
from apds9960 import  APDS9960
import pyrebase
import smbus
import datetime
import requests,json

port = 1
bus = smbus.SMBus(port)

apds = APDS9960(bus)

url = 'https://us-central1-personify-c98fc.cloudfunctions.net/postDeviceData'

dirs = {
    APDS9960_DIR_NONE: "none",
    APDS9960_DIR_LEFT: "left",
    APDS9960_DIR_RIGHT: "right",
    APDS9960_DIR_UP: "up",
    APDS9960_DIR_DOWN: "down",
    APDS9960_DIR_NEAR: "near",
    APDS9960_DIR_FAR: "far",
}

config = {
  "apiKey": " ",
  "authDomain": " ",
  "databaseURL":"https://firstpy-b9b91-default-rtdb.firebaseio.com",
  "storageBucket": " "  
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

apds.setProximityIntLowThreshold(100)
now=datetime.datetime.now()
print("Today date:{}".format(now.strftime("%Y-%m-%d %H:%M:%S")))

print("Gesture Test")
print("============")
apds.enableGestureSensor()

while True:
    sleep(0.5)
    if apds.isGestureAvailable():
        motion = apds.readGesture()
        disp = "{}".format(dirs.get(motion, "unknown"))
        print("Gesture={}".format( disp)) 
        db.child("data").child("newdata").update({"movement":disp})
        
        data= {"uid":'XHVfPr23F7Meg0QuwEkYFvI8Fqd2',"accessCode":"apple",
        "DATA":{'value':disp,'type':"GESTURE"}
        }
        headers = {'Content-type':'application/json','Accept':'text/plain'}

        x = requests.post(url, data=json.dumps(data), headers=headers)

        print(x.text)

