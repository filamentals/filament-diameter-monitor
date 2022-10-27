from time import sleep
from picamera import PiCamera
import globals

cam = PiCamera()
cam.resolution = (globals.XRESOLUTION, globals.YRESOLUTION)
cam.start_preview()
sleep(1000)
cam.close()