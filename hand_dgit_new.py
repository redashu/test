#!/usr/bin/python3
from sklearn.datasets import load_digits
import matplotlib.pyplot  as plt
from  sklearn.model_selection  import  train_test_split
from  sklearn.svm  import  SVC
import numpy   as np
#  importing  dataset of digit
digit=load_digits()
print(dir(digit))
'''
#  descr 
#print(digit.DESCR)
print(digit.target_names)
print(digit.target[9])
print(digit.data.shape)
# now time for image 
print(digit.images[0])
plt.imshow(digit.images[9])
plt.show()
'''
#  training  data 
train_data=np.delete(digit.data,-1,axis=0)
test_data=digit.data[-1]
train_target=np.delete(digit.target,-1,axis=0)
test_target=digit.target[-1]



#  calling  SVM where we are using  SVC 
clf=SVC()
svc_trained=clf.fit(train_data,train_target)
#  
output=svc_trained.predict(test_data.reshape(1,64))
print(output)
print(test_target)
plt.imshow(digit.images[-1])
plt.show()






