#!/usr/bin/python3

import  cv2
import numpy  as  np
print(cv2.__version__)

# now reading image 
#  image flags                       1
dog_img=cv2.imread('dog1.jpg')
t_img=cv2.imread('t.jpg')
#adimg=cv2.add(dog_img,t_img)
#t_dog=dog_img+t_img               gamma -- 0 /  1
t_dog=cv2.addWeighted(dog_img,0.2,t_img,0.7,0)
cv2.imshow('td',t_dog)
cv2.imshow('td1',adimg)
cv2.waitKey(0)




