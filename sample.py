from typing import Counter
import numpy as np
import cv2

img = cv2.imread('test_image_1.png')
imGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh1 = cv2.threshold(imGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('Binary Threshold', thresh1)
hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image', hsvimg)
i =0
li =[]
li1=[]

for contour in contours:
    if i==0:
        i=1
        continue

    approx =  cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True),True)
    M= cv2.moments(contour)
    if M['m00']!=0.0:
        x = int(M['m10']/M['m00'])
        y= int(M['m01']/M['m00'])

    
    li1.append(x)
    li1.append(y)
    if len(approx)==3:
        li.append('Triangle')
    elif len(approx)==4:
        li.append('Quadrangle')
    elif len(approx)==5:
        li.append('Pentagon')
    elif len(approx)==6:
        li.append('Hexagon')
    else:
        li.append('Circle')

print(li)
print(li1)
cv2.imshow("test_image_1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

