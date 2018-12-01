import numpy as np 
import cv2

def cartesian_coordinates(sx, sy, fw, fh):
    cx = sx - (fw/2)
    cy = (fh/2) - sy

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    f_width = cap.get(3)
    f_height = cap.get(4)
    print (f_width, f_height)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x,y,w,h) in faces:
        print (x,y,w,h)

        rect_color = (255,0,0)
        stroke = 2
        end_x = x + w
        end_y = y + h
        cv2.rectangle(frame, (x,y), (end_x,end_y), rect_color, stroke)
    

    cv2.imshow('WebCam',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()