#imports
from vcgencmd import Vcgencmd
import pyrebase
import time

#firebase
config = {
  "apiKey": "AIzaSyC42ryHyiziZbOVNHCNxmCso0_vGt0bW90",
  "authDomain": "voltagereaderpersonify.firebaseapp.com",
  "databaseURL": "https://voltagereaderpersonify-default-rtdb.firebaseio.com",
  "storageBucket": "voltagereaderpersonify.appspot.com"
  
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
#loop 5 second increments

while True:
  #function call to read core coltage
    vcgm = Vcgencmd()
    output = vcgm.measure_volts("core")
   
   #stores variable in output
    print(output)
   
   #stores output in data under core voltage in firebase
    data = {"corevoltage": output}

    #creates child under core voltage and stores data under reading
    db.child("reading").set(data)
    time.sleep(5)
