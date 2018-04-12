import cv2
import numpy as np

def Recognition():
    directory = 'C:/Users/andre/Desktop/world domination/AI/opencv/face recog/Personal/AI/'
    faceDetect = cv2.CascadeClassifier(directory+'haarcascade_frontalface_default.xml');
    cam = cv2.VideoCapture(0)
    print('\n\n\npress "Q" on the "Camera Window" to end\n\n')

    while(True):
        ret, img = cam.read();
        grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
        faces = faceDetect.detectMultiScale(grayScale,1.3,5);
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("Face Recognition", img);
        if cv2.waitKey(1)==ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
