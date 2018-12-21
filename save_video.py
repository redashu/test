#!/usr/bin/python3

import  cv2
#  starting camera 
cap=cv2.VideoCapture(0)
# what is the format of frame support by opencv 
cv_decoder=cv2.VideoWriter_fourcc(*'XVID')
#  creating avi file format to save video using above decoder
#                 file name    decoder  FPS  , resolution 
v_out=cv2.VideoWriter('myclass.avi',cv_decoder,120,(640,480))

while cap.isOpened():
	status,frame=cap.read()
	#f_img=cv2.flip(frame,0)
	cv2.imshow('live',frame)
	v_out.write(frame)
	if cv2.waitKey(2) &  0xFF == ord('q') :
		break 

cv2.destroyAllWindows()
v_out.release()
cap.release()
