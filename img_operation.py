#!/usr/bin/python

import  cv2
#  checking version 
print  cv2.__version__
# reading image from jpeg file
img_data=cv2.imread('kat.jpeg')
img_data1=cv2.imread('kat.jpeg',0)
print img_data

print type(img_data)
print  img_data.shape
# creating new image 
cv2.imwrite('newkat50.jpg',img_data-50)
cv2.imwrite('newkat30.jpg',img_data-30)
cv2.imwrite('newkat10.jpg',img_data-10)
cv2.imwrite('newkat150.jpg',img_data-150)
cv2.imwrite('newkatp50.jpg',img_data+50)
cv2.imwrite('newkatcolorless.jpg',img_data1)

