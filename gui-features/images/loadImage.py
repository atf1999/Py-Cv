import numpy as np
import cv2

#load img as a grayscale
img = cv2.imread("fab.png", 0)
#create window
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
#wait for a key
cv2.waitKey(0)
#load image
cv2.imshow("Image", img)
cv2.waitKey(0)
#close window
cv2.destroyAllWindows()
