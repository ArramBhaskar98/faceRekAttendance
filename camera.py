from picamera import PiCamera
from time import sleep
import sys

print sys.argv[0]

filename = "/home/pi/Desktop/"
filename += sys.argv[1]
filename += ".jpg"

print filename

camera = PiCamera()
camera.rotation = 180
camera.start_preview()
#for i in range(5):
sleep(2)
camera.capture(filename)
camera.stop_preview()

