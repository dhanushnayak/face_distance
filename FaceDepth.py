import cvzone
import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)



while(True):
    sus,img = cap.read()
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

        


    cv2.imshow("img",img)
    cv2.waitKey(1)
    