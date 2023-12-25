from msslib import type_string
import cv2 as np
import numpy as np
import face_recognition
import os
from datetime import datetime

# Reading images from image directory
path = "Attendance/Images"
images = []
personName = []
myList = os.listdir(path)

print(myList)

for cu_img in myList:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_Img)
    personName.append(os.path.splitext(cu_img)[0])
    
print(personName)

def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
    
encodeListKnown = faceEncodings(images)
print('Encoding Complete')

def attendance(name):
    with open('Attendance/Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList=[]
        for line in myDataList:
            entry=line.split(',')
            nameList.append(entry[0])
            
            if name not in nameList:
                time_now=datetime.now()
                dstr=time.now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dstr}')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    faces = cv2.resize(frame,(0,0),None,0.25,0.25)
    faces = cv2.cvtColor(faces,cv2.COLOR_BGR2RGB)

    encodesCurFrame = face_recognition.face_encodings(faces)
    matches = face_recognition.compare_faces(encodeListKnown,encodeFace)

    for matchIndex in loc:
        name = classNames[matchIndex].upper()

        y1,x2,y2,x1 = faceLoc
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0), 2)
        cv2.putText(img,name,(x1+6,y1-6),cv.FONT_HERSHEY_COMPLEX,.5,(255))

        markAttendance(name)

cv.imshow('Camera',img)
if cv.waitKey(10) == 13:
    break

cap.release()
cv.destroyAllWindows()
