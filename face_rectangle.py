#!/usr/bin/python3

import cv2

cap=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier('face.xml')
print(dir(cascade))

while cap.isOpened():
	status,frame=cap.read()
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=cascade.detectMultiScale(gray_frame,1.5,5)
	print(faces)
	for  (x,y,w,h) in  faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		#  gray face image data
		gray_region_face=gray_frame[y:y+h,x:x+w]
		#  original face image data
		origin_region_face=frame[y:y+h,x:x+w]

	cv2.imshow('live',frame)

	if cv2.waitKey(2) &  0xFF == ord('q') :
		break
cv2.destroyAllWindows()
cap.release()
