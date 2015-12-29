import cv2
import numpy as np

img = cv2.imread("plant.jpg",0)
kernel = np.ones((5,5),np.uint8)
morph = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

cv2.imshow("morph gradient",morph)
cv2.waitKey(0)
cv2.destroyAllWindows()

