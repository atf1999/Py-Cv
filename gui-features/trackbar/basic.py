import numpy as np
import cv2

def nothing(x):
    pass

#black img and window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

#trackbars
#Title txt, window it belongs to, startVal, endVal
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)

#on off bar
switch = "0: OFF\n1 : ON"
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
       break
    
    #get current postions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch, 'image')
   
    #if on, set color to trackbars
    #if off, set color to zero
    if s:
        img[:] = [b,g,r]
    else:
        img[:] = 0
cv2.destroyAllWindows()
