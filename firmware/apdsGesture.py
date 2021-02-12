from time import sleep
import firebase
from apds9960.const import *
from apds9960 import  APDS9960
import pyrebase
import smbus

port = 1
bus = smbus.SMBus(port)

apds = APDS9960(bus)

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
now=datetime.now()
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
