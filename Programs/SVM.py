
# coding: utf-8

# In[68]:


# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from sklearn.metrics import accuracy_score


# In[32]:


#load csv file
x=pd.read_csv("D:\\SVM.csv")
X=np.array(x)
y=X[:,2]                          # extract label vector from csv file
x=X[:,[0,1]]                      # extract two feature vector from csv file
print (x),(y)                     # print feature vector and label vector seperately


# In[40]:


#split data into training and test set
def shuffle(X):                            
 random.shuffle(X)                         # shuffle data in X
 train_data = X[:int(0.7*100)]             #change the length of data
 test_data = X[int(0.7*100):]
 return train_data, test_data


# In[43]:


train_dataset, test_dataset = shuffle(X)
a=train_dataset[:,[0,1]]                   # feature vector of training set
b=train_dataset[:,2]                       # label vector of training set
p=test_dataset[:,[0,1]]                    # feature vector of test set
q=test_dataset[:,2]                        # label vector of test set


# In[31]:


# plotting scatters 
plt.scatter(X[:, 0], X[:, 1], c=y, s=50);
plt.show()


# In[89]:


# import support vector classifier
from sklearn.svm import SVC                # "Support Vector Classifier"
clf = SVC(kernel='linear')                 # SVC using linear kernel
clf1 = SVC(kernel='rbf')                   # SVC using RBF kernel


# In[80]:


# fitting x samples and y classes
clf.fit(a, b)


# In[82]:


P=clf.predict(p)

print P  #P is the predicted class (0,1,2,3 0r 4)
print q  #q is the class value in test set

print "Accuracy:",accuracy_score(q,P)


# In[86]:


clf1.fit(a,b)


# In[87]:


P1=clf1.predict(p)

print P  #P is the predicted class (0,1,2,3 0r 4)
print q  #q is the class value in test set

print "Accuracy:",accuracy_score(q,P1)

