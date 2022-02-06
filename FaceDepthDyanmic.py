import cvzone
import cv2
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
textList = ["Welcome to WorkShop.","Study CV, and AI"]


while(True):
    sus,img = cap.read()
    imgText = np.zeros_like(img)
    img,faces=detector.findFaceMesh(img,draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        
        cv2.circle(img,pointLeft,5,(255,0,255),cv2.FILLED)
        cv2.circle(img,pointRight,5,(255,0,255),cv2.FILLED)
        cv2.line(img,pointLeft,pointRight,(0,200,0),4)

        """# finding Focal = f = (w*d) / W
        w,_ = detector.findDistance(pointLeft,pointRight)
        W = 6.3
        d=15
        f= (w*d)/W
        print(f)

        #finding distance  f = 550"""

        #FIND DISTANCE
        w,_ = detector.findDistance(pointLeft,pointRight)
        W = 6.3
        f=550
        d = int((W*f)/w)
        forehead = face[10]
        cvzone.putTextRect(img,f'D = {d}',
        (forehead[0]-75,forehead[1]-50),
        scale=2)

        for i,text in enumerate(textList):
            singleHeight = 20 +int(round(d)/4)
            scale = 0.4 + (int(d/10) *10)/75
            cv2.putText(imgText,text,(50,50+((i+1)*singleHeight)),cv2.FONT_ITALIC,scale,(255,255,255),2)

        

    imgStacked = cvzone.stackImages([img,imgText],2,1)
    cv2.imshow("img",imgStacked)
    cv2.waitKey(1)
    