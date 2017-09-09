# iotHack

Facerek is a system that uses face recognition to automate the attendance system.

It makes use of a Raspberry Pi Model 3B and a Raspberry Pi Camera Module (V2) to capture
images of the classroom and then segments the image into 5 different sections.
Amazon's 'Rekognition' API is then used to detect faces in each segment. When a face is identified,
the section of the image corresponding to the face is compared against the training set to find matches.

When a match is found, a database is updated to indicate the presence of the student in class.
To avoid misidentification and other such error, pictures are taken every 5 minutes and the results are
compared to confirm the student's presence.




