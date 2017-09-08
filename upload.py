import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from PIL import Image
from picamera import PiCamera
from time import sleep
import sys

import os

from datetime import datetime

filename = "";

d = datetime.now()
filename = str(d.isoformat())


print filename

os.system("python ./camera.py " + filename)

img = Image.open(filename+'.jpg', mode = 'r')

width, height = img.size
width = 2*width
height = 2*height
img = img.resize((width, height))

img_crop1 = img.crop((0, 0 , 0.6*width , 0.6*height))
img_crop2 = img.crop((0, 0.4*height, 0.6*width, height))
img_crop3 = img.crop((0.4*width, 0, width, 0.6*height))
img_crop4 = img.crop((0.4*width, 0.4*height, width, height))
img_crop5 = img.crop((0.2*width, 0.2*height, 0.8*width, 0.8*height))


img_crop1.save(filename + 'part' + '1' + '.jpg')
img_crop2.save(filename + 'part' + '2' + '.jpg')
img_crop3.save(filename + 'part' + '3' + '.jpg')
img_crop4.save(filename + 'part' + '4' + '.jpg')
img_crop4.save(filename + 'part' + '5' + '.jpg')

conn = boto.connect_s3()
b = conn.get_bucket('classimages')
k = Key(b)

for i in range(0,5):
    
    k.key = filename + 'part' + str(i+1) + '.jpg'
    k.set_contents_from_filename('/home/pi/Desktop/' + filename + 'part' + str(i+1) + '.jpg')

b = conn.get_bucket('backuprvce')
k = Key(b)
k.key = filename + '.jpg'
k.set_contents_from_filename('/home/pi/Desktop/' + filename + '.jpg')
