import numpy as np
import cv2
#load color image as Grayscale
img = cv2.imread('fab.png', 0)
#display image
cv2.imshow('Image', img)
#waits for a key to be pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
