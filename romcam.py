# import packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize camera
camera = PiCamera()
rawCap = PiRGBArray(camera)
time.sleep(0.1)
