#imports
from vcgencmd import Vcgencmd
import pyrebase
import time
import requests
import json

#loop 5 second increments

while True:
  #function call to read Voltage Sensor output
    vcgm = Vcgencmd()
    output = vcgm.measure_volts("core")
 
    
   #stores variable in output
    print(output)
   

#pushing to personify database
    url = "https://us-central1-personify-c98fc.cloudfunctions.net/postDeviceData"
    data = {
        "uid": "XHVfPr23F7Meg0QuwEkYFvI8Fqd2",
        "accessCode": "apple",
        "DATA": {
        "value": output,
        "type": "CORE_VOLTAGE"
        }
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

#status confirmation text
    print(r.text)


#run every 10 secs
    time.sleep(10)
