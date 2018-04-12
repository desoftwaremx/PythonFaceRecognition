import os, cv2
import numpy as np
from PIL import Image



recognizer = cv2.face.LBPHFaceRecognizer_create()
path = './DataSet'

def getImagesWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePaths in imagePaths:
        faceImg = Image.open(imagePaths).convert('L');
        faceNp = np.array(faceImg,'uint8');
        ID = int(os.path.split(imagePaths)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow('training',faceNp)
        cv2.waitKey(10)
    return IDs, faces

def Train():
    try:
        Ids, faces = getImagesWithID(path)
        recognizer.train(faces,np.array(Ids))
        recognizer.save('./Training/trainingData.yml')
        cv2.destroyAllWindows()
        print('Train Succeed')
    except:
        print('Train failed')
