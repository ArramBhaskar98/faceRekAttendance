import os
import sys
import boto3
import json
import base64
from PIL import Image
import io
import boto
from io import BytesIO
import time
from boto.s3.key import Key
import botocore




def upload_photo(img):
	conn = boto.connect_s3()
	b = conn.get_bucket('croprvce')
	k = Key(b)
	k.key = img
	k.set_contents_from_filename(img)

#---------------------------------------------------

	

if __name__ == '__main__':
	client = boto3.client('rekognition')

	bucket = 'bucket'
	BUCKET_NAME = 'classimages'
	#KEY = 'kng.JPG'

	#bucket = conn.get_bucket('classimages')
	s3 = boto3.resource('s3')


	classBucket = s3.Bucket(BUCKET_NAME)
	# for object in classBucket.objects.all():
	# 	KEY = str(object.key)
	KEY_LIST = classBucket.objects.all()
	for object in KEY_LIST:
		print(str(object.key))

		

	KEY = '1.jpg'
	for object in KEY_LIST:
		KEY = str(object.key)
		try:
			s3.Bucket(BUCKET_NAME).download_file(KEY, 'local_img.jpg')
		except botocore.exceptions.ClientError as e:
			if e.response['Error']['Code'] == '404':
				print("Object doesn't exist")
			else:
				print("Else error")

		response = client.detect_faces(Image = {"S3Object":{"Bucket":BUCKET_NAME,"Name":KEY}}, Attributes = ['ALL'] )
		#print(response)

		#byteArray = io.BytesIO()
		index = 1
		for face in response["FaceDetails"]:
			img = Image.open("local_img.jpg", mode = 'r')
			width, height = img.size

			left = face["BoundingBox"]["Left"]*width
			upper = face["BoundingBox"]["Top"]*height
			right = left + face["BoundingBox"]["Width"]*width
			lower = upper + face["BoundingBox"]["Height"]*height
			img2 = img.crop((left, upper, right, lower))

			img2.save('img' + str(index) + '.jpg')
			
			img2.show()
			with open('img' + str(index) + '.jpg', 'rb') as image:
				#image.show()
				upload_photo('img' + str(index) + '.jpg')
				try:
					response1 = client.search_faces_by_image(
						CollectionId = 'stud-id',
						Image = {
							'S3Object' : {
								'Bucket':'croprvce',
								'Name':'img' + str(index) + '.jpg'
							}
						}
					)
					print(response1)
				except:
					continue
				
			os.system("aws s3 rm s3://croprvce --recursive")
			os.system("rm "+'img' + str(index) + '.jpg')
			index += 1

	os.system("aws s3 rm s3://classimages --recursive")
	os.system("rm local_img.jpg")


	
