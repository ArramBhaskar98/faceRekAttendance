import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key

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

conn = boto.connect_s3()
b = conn.get_bucket('classimages')
k = Key(b)
k.key = filename + '.jpg'
k.set_contents_from_filename('/home/pi/Desktop/' + filename + '.jpg')
