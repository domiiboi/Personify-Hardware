
#!/usr/bin/env python
# (This is an example similar to an example from the Adafruit fork
#  to show the similarities. Most important difference currently is, that
#  this library wants RGB mode.)
#
# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.
# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm
from os import X_OK, stat
from typing import KeysView
from PIL import Image, ImageDraw, ImageFont, ImageOps
import time, sched, requests, json
import PIL
import numpy as np
from requests.api import put
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
# Configuration for the matrix


options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
#options.chain_length = 1
#options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.scan_mode = 1
options.gpio_slowdown = 4
options.show_refresh_rate = 1
options.limit_refresh_rate_hz = 240
options.pwm_lsb_nanoseconds = 100
matrix = RGBMatrix(options = options)

#fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 6)


def displayStat(matrix, stat, value):


    #Custon light display
    if(stat == "LIGHT"):
        
        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)

        #Setup the two "canvases"
        image = Image.open("images/idea.png").convert("RGB")
        statsImage = Image.new("RGB", (32,32))
        Invertedimage = PIL.ImageOps.invert(image)

        #Display Width & Height
        W,H = (64, 32)

        Invertedimage.thumbnail((28, 28), Image.ANTIALIAS)


        drawStats = ImageDraw.Draw(statsImage)

        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
        #Static text at the top
        w, h = fnt.getsize(stat)
        drawStats.text(((32-w)/2,0), stat, font = fnt, fill=(200,200,200))

        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        previousHeight = h
        w, h = fnt.getsize(str(value))
        drawStats.text(((31-w)/2,previousHeight), str(value), font = fnt, fill=(200,200,200))

        # # pixels[6,9] = (255,255,255)
        matrix.Clear()
        matrix.SetImage(Invertedimage, 2, 2)
        matrix.SetImage(statsImage, 31 ,0)
        time.sleep(2)

        matrix.Clear()


    #Custon temp display
    if(stat == "TEMP"):
        
        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)

        #Setup the two "canvases"
        image = Image.open("images/thermometer.png").convert("RGB")
        statsImage = Image.new("RGB", (32,32))
        Invertedimage = PIL.ImageOps.invert(image)

        #Display Width & Height
        W,H = (64, 32)

        Invertedimage.thumbnail((28, 28), Image.ANTIALIAS)


        drawStats = ImageDraw.Draw(statsImage)

        # fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
        # #Static text at the top
        # w, h = fnt.getsize(stat)
        # drawStats.text(((32-w)/2,0), stat, font = fnt, fill=(200,200,200))

        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
        #previousHeight = h
        w, h = fnt.getsize(str(value) + "°C")
        drawStats.text(((31-w)/2,(H-h)/2), str(value) + "°C", font = fnt, fill=(200,0,0))

        # # pixels[6,9] = (255,255,255)
        matrix.Clear()
        matrix.SetImage(Invertedimage, 2, 2)
        matrix.SetImage(statsImage, 31 ,0)
        time.sleep(2)

        matrix.Clear()


    #Custon VOLT display
    if(stat == "VOLT"):


        statsImage = Image.new("RGB", (64,32))

        W,H = (64, 32)
        

        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
        #Static text at the top
        w, h = fnt.getsize(stat)

        drawStats = ImageDraw.Draw(statsImage)

        drawStats.text(((W-w)/2,0), stat, font = fnt, fill=(200,200,200))

        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
        #previousHeight = h
        w, h = fnt.getsize(str(value))
        drawStats.text(((W-w)/2,(H-h)/2 + 4), str(value), font = fnt, fill=(80,50,200))

        # # pixels[6,9] = (255,255,255)
        matrix.Clear()
        #matrix.SetImage(Invertedimage, 2, 2)
        matrix.SetImage(statsImage, 0 ,0)
        time.sleep(2)

        matrix.Clear()

    #Custon POSTS display
    if(stat == "POSTS"):
        
        statsImage = Image.new("RGB", (64,32))

        W,H = (64, 32)
        

        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
        #Static text at the top
        w, h = fnt.getsize(stat)

        drawStats = ImageDraw.Draw(statsImage)

        drawStats.text(((W-w)/2,0), stat, font = fnt, fill=(200,200,200))

        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
        #previousHeight = h
        w, h = fnt.getsize(str(value))
        drawStats.text(((W-w)/2,(H-h)/2 + 4), str(value), font = fnt, fill=(200,20,80))

        # # pixels[6,9] = (255,255,255)
        matrix.Clear()
        #matrix.SetImage(Invertedimage, 2, 2)
        matrix.SetImage(statsImage, 0 ,0)
        time.sleep(2)

        matrix.Clear()

    #Custon temp display
    if(stat == "FOLLOWERS"):
        
        statsImage = Image.new("RGB", (64,32))

        W,H = (64, 32)
        

        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)

        w, h = fnt.getsize(stat)

        drawStats = ImageDraw.Draw(statsImage)

        drawStats.text(((W-w)/2,0), stat, font = fnt, fill=(200,200,200))

        fnt = ImageFont.truetype("/user/share/fonts/truetype/DejaVuSans", 13)
        #previousHeight = h
        w, h = fnt.getsize(str(value))
        drawStats.text(((W-w)/2,(H-h)/2 + 4), str(value), font = fnt, fill=(200,200,200))

        # # pixels[6,9] = (255,255,255)
        matrix.Clear()
        #matrix.SetImage(Invertedimage, 2, 2)
        matrix.SetImage(statsImage, 0 ,0)
        time.sleep(2)

        matrix.Clear()

    
    #Custon VOLT display
    if(stat == "LIKES"):


        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)

        #Setup the two "canvases"
        image = Image.open("images/like.png").convert("RGB")
        statsImage = Image.new("RGB", (32,32))
        Invertedimage = PIL.ImageOps.invert(image)

        #Display Width & Height
        W,H = (64, 32)

        Invertedimage.thumbnail((28, 28), Image.ANTIALIAS)


        drawStats = ImageDraw.Draw(statsImage)

        # fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
        # #Static text at the top
        # w, h = fnt.getsize(stat)
        # drawStats.text(((32-w)/2,0), stat, font = fnt, fill=(200,200,200))

        fnt = ImageFont.truetype("/user/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
        #previousHeight = h
        w, h = fnt.getsize(str(value))
        drawStats.text(((31-w)/2,(H-h)/2), str(value), font = fnt, fill=(200,200,200))

        # # pixels[6,9] = (255,255,255)
        matrix.Clear()
        matrix.SetImage(Invertedimage, 2, 2)
        matrix.SetImage(statsImage, 31 ,0)
        time.sleep(2)

        matrix.Clear()

    



while True:
    print("Getting data and refreshing view")
    url = "https://us-central1-personify-c98fc.cloudfunctions.net/getDeviceData"

    data = {
        "uid": "XHVfPr23F7Meg0QuwEkYFvI8Fqd2",
        "accessCode": "apple"
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    #print(r.text)


    values = json.loads(r.text)

    dataObject = values['data']
    #print(dataObject)

    coreVoltage = 0;
    temperature = 0;
    light = 0;
    numOfFollowers = 0;
    percentOfLikes = 0;
    numOfPosts = 0;

    print('\n')
    #print(dataObject)
    for x in dataObject:
        #print(x);
        for keys in x:
            if(keys == 'LIGHT_SENSOR'):
                obj = x[keys]
                light = obj['value']
                print('Light value: ', obj['value'])
                displayStat(matrix, "LIGHT", light)

            if(keys == 'TEMPERATURE'):
                obj = x[keys]
                temperature = obj['value']
                print('Temperature value: ', obj['value'])
                displayStat(matrix, "TEMP", temperature)
            
            if(keys == 'CORE_VOLTAGE'):
                obj = x[keys]
                coreVoltage = obj['value']
                print('Core voltage value: ', obj['value'])
                displayStat(matrix, "VOLT", coreVoltage)
            
            if(keys == 'numOfPosts'):
                obj = x[keys]
                numOfPosts = obj
                print('Number Of Posts: ', str(obj))
                displayStat(matrix, "POSTS", numOfPosts)

            if(keys == 'numOfFollowers'):
                obj = x[keys]
                numOfFollowers = obj
                print('Number of Followers: ', str(obj))
                displayStat(matrix, "FOLLOWERS", numOfFollowers)
            
            if(keys == 'percentOfLikes'):
                obj = x[keys]
                percentOfLikes = obj
                print('Percent of likes: ', str(obj))
                displayStat(matrix, "LIKES", percentOfLikes)



