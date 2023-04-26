
import cv2
vid = cv2.VideoCapture(0)
while True:
    ret,frame = vid.read()
    image = cv2.putText(frame,"welcome to ML class",(50,70),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),5)
    cv2.imshow('my live video',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('iam here')
        pass
        vid.release()
        cv2.destroyAllWindows()










