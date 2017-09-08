import os
import sys

os.system("aws rekognition detect-faces --image '{\"S3Object\":{\"Bucket\":\"classimages\",\"Name\":\"kng.JPG\"}}' --region us-east-1 --profile user1")

