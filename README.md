# iotHack

## Facerek is a system that uses face recognition to automate the attendance system.

It makes use of a Raspberry Pi Model 3B and a Raspberry Pi Camera Module (V2) to capture
images of the classroom and then segments the image into 5 different sections.
Amazon's 'Rekognition' API is then used to detect faces in each segment. When a face is identified,
the section of the image corresponding to the face is compared against the training set to find matches.

When a match is found, a database is updated to indicate the presence of the student in class.
To avoid misidentification and other such error, pictures are taken every 5 minutes and the results are
compared to confirm the student's presence.

### Prerequisite steps
The AWS indexFaces command is used to upload quality images which are used as the basis for the face recognition model.
An SQL database is set up on Azure.


### camera.py
This file clicks pictures at regular intervals using the Raspberry Pi Camera.

### upload.py
This file uploads the captured images to the Amazon S3 storage service.

### detect.py
1. Faces in the image are detected using AWS Rekognition
2. Based on the markers returned, the individual faces are cropped and resized
3. Each face is searched against known images in the collection on Rekognition
4. The response is evaluated to discover any matching faces

### insertDB.py
Add an entry into the database, USN is passed as a parameter

### updateDB.py
This file updates the attendance database. The USN is an argument, and the attendance is marked based on the time automatically.

### viewDB.py
Retrieve the 
