#!/usr/bin/python3

from  sklearn  import  tree

#print(dir(tree))
# creating dataset for apple/orange
# we are calculating weight and texture 
# smooth is 0 and bumpy is 1
features=[[120,0],[140,0],[150,1],[170,1]]
label=["apple","apple","orange","orange"]

# now calling  decision tree algo
algo=tree.DecisionTreeClassifier()
# time for training data
trained=algo.fit(features,label)

# now prediction 
output=trained.predict([[148,0],[135,1]])
print(output)







