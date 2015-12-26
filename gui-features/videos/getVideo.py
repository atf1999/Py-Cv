import numpy as np
import cv2

#Video object
cap = cv2.VideoCapture(0)

while(True):
    #Capture frame by frame
    ret, frame = cap.read()
    
    #convert to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    #Display resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release the camera when done
cap.release()
cv2.destroyAllWindows()
