import cv2
import numpy as np
from Connection.userController import GetUser


def Recognition():

    faceDetect = cv2.CascadeClassifier('./Function/haarcascade_frontalface_default.xml');
    cam = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create();
    rec.read("./Training/trainingData.yml")
    id = 0;
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontcolor = (255, 0, 0)
    fontscale = 0.5

    print('\n\n\npress "Q" on the "Camera Window" to end\n\n')

    while(True):
        ret, img = cam.read();
        grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
        faces = faceDetect.detectMultiScale(grayScale,1.3,5);
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            id,conf = rec.predict(grayScale[y:y+h, x:x+w])
            name, age, gender, desc = GetUser(id)
            if name != None:
                cv2.putText(img, name, (x+w,y+10), font, fontscale, fontcolor);
                cv2.putText(img, age, (x+w,y+15+10), font, fontscale, fontcolor);
                cv2.putText(img, gender, (x+w,y+30+10), font, fontscale, fontcolor);
                cv2.putText(img, desc, (x+w,y+45+10), font, fontscale, fontcolor);
        cv2.imshow("Face Recognition", img);
        if cv2.waitKey(1)==ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
