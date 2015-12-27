import numpy as np
import cv2

img = cv2.imread('fab.png')

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow("scaled", res)
cv2.waitKey()
cv2.destroyAllWindows()
