#!/usr/bin/python3

import  cv2
import numpy  as  np
print(cv2.__version__)

# now reading image 
#  image flags                       1
color_img=cv2.imread('dog1.jpg',cv2.IMREAD_COLOR)
#color_img=np.zeros((512,512,3))
#           window name , img data
print(color_img.shape)
# this is ROI 
#cv2.imshow('cimg',color_img[200:400,200:700])
# now time for  basic image operations 
# draw a line BGR                     
cv2.line(color_img,(0,0),(300,400),(0,0,255),10)
# rectangle
cv2.rectangle(color_img,(0,0),(200,320),(0,255,0),-1)
# circle
cv2.circle(color_img,(400,500),60,(255,0,0),-1)
# font type set 
font = cv2.FONT_HERSHEY_SIMPLEX
#                                              font_size      font_line_width
cv2.putText(color_img,'OpenCV',(10,20), font, 6,(255,255,255),8,cv2.LINE_AA)

cv2.imshow('newimg',color_img)
cv2.waitKey(0)




