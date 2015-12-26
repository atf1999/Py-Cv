import numpy as np
import cv2

img = cv2.imread('fab.png', 0)
cv2.imshow("Save image demo", img)
k = cv2.waitKey(0) & 0xFF
#if esc key is pressed
if k == 27:
    cv2.destroyAllWindows
#if s key is pressed
elif k == ord('s'):
    #save image
    cv2.imwrite("fab1.png", img)
    print "img saved"
    cv2.destroyAllWindows()
