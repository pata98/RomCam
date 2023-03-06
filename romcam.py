# import packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import sleep

# initialize camera
camera = PiCamera()
time.sleep(0.1)
camera.start_preview()
sleep(5)

camera.capture('image1.jpg')
camera.stop_preview()