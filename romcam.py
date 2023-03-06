# import packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import sleep

# initialize camera
camera = PiCamera()
time.sleep(0.1)

camera.capture('image1.jpg')