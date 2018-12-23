#!/usr/bin/python3

# laoding  iris dataset from  sklearn 
from sklearn.datasets import load_iris
# loading  tree factor for decisiontree Classifier 

# loading  dataset 
iris=load_iris()
print(dir(iris))

'''
 dataset explaination 
here features store under ---->   iris.data
     label               ---->    iris.target - 0 mean setosa , 1 versicolor                                                 2 - virginica 

iris.target_names == contains flower name
iris.feature_names = contains flower attribute 

'''      
# split datasets into training and testing 
#                  features ,  label      testsize 10%
from sklearn.model_selection import  train_test_split
train_data,test_data,train_target,test_target=(train_test_split(iris.data,iris.target,test_size=0.1))

train_data1,test_data1,train_target1,test_target1=(train_test_split(iris.data,iris.target,test_size=0.2))
print(test_data.shape)
print(test_target.shape)
'''
above train_data -- training features that is 90%
      test_data ---- remaining  10%  of  data that you can use to test 
      train_target --- training label that is  90% 
      test_target ----  remaining  10%  of label 


'''
# loading KNN 
from  sklearn.neighbors  import  KNeighborsClassifier
clf=KNeighborsClassifier(n_neighbors=5)
trained=clf.fit(train_data,train_target)
output=trained.predict(test_data)
print(output)

'''

# calculating  accuracy for  decisiontree 
from  sklearn.metrics  import  accuracy_score
acc10=accuracy_score(test_target,output10)
acc20=accuracy_score(test_target1,output20)
print("accuracy of DSC Tree with 10 % ",acc10)
rint("accuracy of DSC Tree with 20%  ",acc20)
'''
