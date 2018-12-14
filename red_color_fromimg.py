#!/usr/bin/python3

import cv2

# reading image 
img=cv2.imread('index.png',1)
only_red=cv2.inRange(img,(0,0,40),(20,20,255))
cv2.imshow('red',only_red)
cv2.waitKey(0)

cv2.destroyAllWindows()
