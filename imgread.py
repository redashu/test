#!/usr/bin/python3

import  cv2
print(cv2.__version__)

# now reading image 
#  image flags                       1
color_img=cv2.imread('dog1.jpg',cv2.IMREAD_COLOR)
#                                  0
gray_img=cv2.imread('dog1.jpg',cv2.IMREAD_GRAYSCALE)
#                                    -1
unch_img=cv2.imread('dog1.jpg',cv2.IMREAD_UNCHANGED)
#  display image 
#           window name , img data
cv2.imshow('cimg',color_img)
#cv2.imshow('gimg',gray_img)
#cv2.imshow('uimg',unch_img)
# to hold window 
cv2.waitKey(0)




