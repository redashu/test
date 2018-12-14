#!/usr/bin/python3

import  cv2

cap=cv2.VideoCapture(0)


print(dir(cap))
#print(cap.isOpened())

'''
while  cap.isOpened()  :
	# start taking frame 
	status,frame=cap.read()
	# converting image to grayscale 
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	# here frame is real image 
	print(frame)
	cv2.rectangle(frame,(40,40),(200,300),(0,255,0),3)
	cv2.imshow('color',frame)
	cv2.imshow('gray',gray_frame)
	if cv2.waitKey(2) & 0xFF  == ord('q') :
		break
	#  additional support 
	elif  cv2.waitKey(2) & 0xFF == ord('c') :
		cv2.imwrite('liveimg.jpg',gray_frame)
		cv2.destroyAllWindows()

'''
cv2.destroyAllWindows()
cap.release()



