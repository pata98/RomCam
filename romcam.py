# import packages
#from picamera.array import PiRGBArray
from RPi.GPIO as GPIO
from picamera import PiCamera
import time

#### DEFINE PIN NUMBER ####
shutter = 1
led = 2

### init
# Camera
camera = PiCamera()
# GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(shutter, GPIO.IN, pull_up_down=GPIO.PUD.UP)

# main
while True:
    if GPIO.input(shutter)
        time.sleep(0.1)
    else:
        camera.capture('image1.jpg')
        GPIO.output(led, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)
        

# Exit, clear GPIO settings
GPIO.clearup()