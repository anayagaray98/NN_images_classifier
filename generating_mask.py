import cv2
import numpy as np

img = cv2.imread('1.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
blue_only = cv2.bitwise_and(img,img, mask= mask)

im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#draw contours with indexes and save coordinates to a txt file
with open('coords.txt', 'w+') as f:
    for i,cnt in enumerate(contours):
        cv2.drawContours(blue_only, cnt, -1, (0,0,255), 1)
        cv2.putText(blue_only, str(i), (cnt[0][0][0], cnt[0][0][1]),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 1)
        f.writelines("contour " + str(i) +" :" + str(cnt))  

cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('blue_only',blue_only)