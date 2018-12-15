#!/usr/bin/python3

import  cv2

#  start camera
cap=cv2.VideoCapture(0)

# capture 3 consecutive frames
take_frame1=cap.read()[1]
take_frame2=cap.read()[1]
take_frame3=cap.read()[1]

#  converting all 3 frames to grayscale
gray_img1=cv2.cvtColor(take_frame1,cv2.COLOR_BGR2GRAY)
gray_img2=cv2.cvtColor(take_frame2,cv2.COLOR_BGR2GRAY)
gray_img3=cv2.cvtColor(take_frame3,cv2.COLOR_BGR2GRAY)

#  creating function for making image as abs diff
def  myimg_diff(x,y,z):
	diff1=cv2.absdiff(x,y)
	diff2=cv2.absdiff(y,z)
	final_diff=cv2.bitwise_and(diff1,diff2)
	return final_diff
#   reading further frames 

while  cap.isOpened():
	status,frame=cap.read()
	#  calling function
	diff_imgdata=myimg_diff(gray_img1,gray_img2,gray_img3)
	# replacing frames 
	gray_img1=gray_img2
	gray_img2=gray_img3
	gray_img3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('motion',diff_imgdata)
	if cv2.waitKey(2) &  0xFF == ord('q'):
		break 


cv2.destroyAllWindows()
cap.release()

