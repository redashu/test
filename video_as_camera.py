#!/usr/bin/python3

import  cv2
#  starting camera 
cap=cv2.VideoCapture('myclass20.avi')

while cap.isOpened():
	status,frame=cap.read()
	#f_img=cv2.flip(frame,0)
	cv2.imshow('live',frame)
	if cv2.waitKey(2) &  0xFF == ord('q') :
		break 

cv2.destroyAllWindows()
v_out.release()
cap.release()
