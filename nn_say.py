#!/usr/bin/python3

import numpy  as np
import os

#flower data set
'''
color: rflwr - bflwr  - rflwr - bflwr - rflwr - bflwr - rflwr - bflwr -- ???
lenght: 3        2       4       3      3.5      2      5.5       1      4.5 	
width:  1.5      1       1.5     1      .5       .5     1         1       1
'''
phrases=['seems like its','i guess','i think','possibly','looks like','guessing']


# define nn
def  NN(m1,m2,w1,w2,b):
	z=m1*w1+m2*w2+b
     # m1 and m2 are values 
     #  random weights w1 and w2
     # b is bias 
	return sigmoid(z)
	#  Note  sigmoid only return answer between 0 to 1 
        # sigmoid(z) =  1/(1+exp(-z)) --we can find graph on google 

#  now defining sigmoid()
def  sigmoid(x):
	return 1/(1+np.exp(-x))

	
# generating random numbers 
w1=np.random.randn()
w2=np.random.randn()
b=np.random.randn()
predict=NN(3,1.5,w1,w2,b)
predict_text=["blue","red"][int(np.round(predict))]
phrase=np.random.choice(phrases)+" "+predict_text

print(phrase)
vo=os.system("say "+phrase)

