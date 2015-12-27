import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):
    #take each frame
    _, frame = cap.read()
  
    #convert bgr to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #define range of blue color in hsv
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    #Threshold the hsv image for blue only
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
   
    #bitwise-and mask and original color
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()

