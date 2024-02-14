import cv2

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

img=cv2.imread('ronny_kb9.jpg')

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = haar_cascade.detectMultiScale(grayImg,1.3,1)
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h), (255,255,0),5)
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyAllWindows()
