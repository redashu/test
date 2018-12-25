#!/usr/bin/python3
from sklearn.datasets import load_digits
import matplotlib.pyplot  as plt
from  sklearn.model_selection  import  train_test_split
from  sklearn.svm  import  SVC
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
# spliting  training and testing data
train_data,test_data,train_target,test_target=train_test_split(digit.data,digit.target,test_size=0.1,random_state=0)

#  calling  SVM where we are using  SVC 
clf=SVC()
svc_trained=clf.fit(train_data,train_target)
#  
output=svc_trained.predict(test_data[2].reshape(1,64))
print(output)
print(test_target[2])






