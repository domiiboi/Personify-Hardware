IR Proximity sensor has IR LED as IR transmitter and Photo diode as IR detector. 
The control circuit consists of Op-amp IC LM358 and associated components such as Four 220ohm resistors, 10K ohm resistor, 10k ohm potentiometer and RED LED.

Python code "BuzzerData.py" has integrated IR proximity sensor having RPI with Pyrebase and Firebase DB. 
The code imports Library for GPIO and Pyrebase. Firebase configuration is given with apiKey, authDomain, databaseURL and storageBucket. 
While loop runs repeatedly and activates the buzzer to give sound when the object is detected by the IR sensor. (here object is a person's hand). 
Then, data proximity is set to 1, so the child proximity set to 1 for Firebase. There is sleep time involved for 2sec.

Note: In the python code, IF statement checking IR sensor was not added as it may not be required since IR sensor is connected to RPI on PCB when it is being used. 
Also, the second while loop for GPIO.input(sensor) may not be required as GPIO.input(sensor) is already passed by while true loop, 
i.e sensor is checked already and displaying as object detected when there is a person's hand. 
If we place a second while loop with GPIO.input(sensor), it must be false in order to introduce time delay, 
but as GPIO.input(sensor) has to be true when object is detected so to introduce time delay for each object detected message, it's better to remove second while loop. 


