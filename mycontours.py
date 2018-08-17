import cv2
import numpy as np

img = cv2.imread('img.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
cv2.drawContours(img,contours,0,(0,255,0),3)

cv2.imshow('src',img)

cv2.waitKey(0)
cv2.destroyAllWindows()