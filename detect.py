import os
import sys
import boto3
import json
from PIL import Image

if __name__ == '__main__':
	client = boto3.client('rekognition')
	bucket = 'bucket'
	BUCKET_NAME = 'classimages'
	KEY = 'kng.JPG'
	s3 = boto3.resource('s3')
	try:
		s3.Bucket(BUCKET_NAME).download_file(KEY, 'local_img.jpg')
	except botocore.exceptions.CLientError as e:
		if e.response['Error']['Code'] == '404':
			print("Object does'nt exist")
		else:
			raise

	response = client.detect_faces(Image = {"S3Object":{"Bucket":"classimages","Name":"kng.JPG"}}, Attributes = ['ALL'] )

	for face in response["FaceDetails"]:
		img = Image.open("local_img.jpg")
		width, height = img.size
		left = face["BoundingBox"]["Left"]*width
		upper = face["BoundingBox"]["Top"]*height
		right = left + face["BoundingBox"]["Width"]*width
		lower = upper + face["BoundingBox"]["Height"]*height
		img2 = img.crop((left, upper, right, lower))
		img2.show()

