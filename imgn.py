#! python27
#import sys
import cv2
#abba.png
#museum.jpg
imagepath = 'museum.jpg'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread(imagepath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.301, 5)
print("Found {0} faces".format(len(faces)))
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(100,200,250),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(200,150,250),2)
cv2.imshow('img',img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
