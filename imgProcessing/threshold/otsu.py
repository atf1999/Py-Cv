import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('plant.jpg',0)

#global thresholding
re1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#otsu threshold
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#otsu threshold after gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#plot images and histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original', 'Histogram', 'Global Thresholding',
          'Original', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered image', 'Histogram', "Otsu's thresholding"]
for i in xrange(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3]),plt.xticks([]),plt.yticks([])

    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)   
    plt.title(titles[i*3+1]),plt.xticks([]),plt.yticks([])

    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2]),plt.xticks([]),plt.yticks([])
plt.show()
