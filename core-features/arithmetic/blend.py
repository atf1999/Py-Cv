import numpy as np
import cv2

#load images
img1 = cv2.imread('twitterimg.png')
img2 = cv2.imread('github.png')

#move image to top left
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

#mask logo and create inverse mask
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
maskInv = cv2.bitwise_not(mask)

#black out area
img1Bg = cv2.bitwise_and(roi,roi,mask=maskInv)

#only region of logo from logo image
img2Fg = cv2.bitwise_and(img2,img2,mask=mask)

#put logo in roi and modify main image
dst = cv2.add(img1Bg,img2Fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows
