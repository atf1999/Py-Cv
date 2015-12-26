import numpy as np
import cv2

#load video from file
cap = cv2.VideoCapture("span.mp4")

#only if video object is open do this operation
while(cap.isOpened()):
    ret, frame = cap.read()
    
    #grayscale img 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #load image
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release video object
cap.release()
cv2.destroyAllWindows()

