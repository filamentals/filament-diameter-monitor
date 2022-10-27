from time import sleep
from picamera import PiCamera
import globals


def get_picture(filename, time2adjust):
    cam = PiCamera()
    cam.resolution = (globals.XRESOLUTION, globals.YRESOLUTION)
    #cam.start_preview()
    sleep(time2adjust)
    cam.capture(filename)
    cam.close()  # take out after the loop is done
