
# coding: utf-8

# In[1]:


import unicodecsv
import random
import math
import operator


# In[2]:


#getdata() function definition
def getdata(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.reader(f)
        return list(reader)


# In[3]:


#split data into training and test set
def shuffle(data):
 random.shuffle(data)
 train_data = data[:int(0.7*100)]             #change the length of data
 test_data = data[int(0.7*100):]
 return train_data, test_data


# In[4]:


#Euclidean distance Calculation
def euclideanDist(x, xi):
 d = 0.0
 for i in range(len(x)-1):
     d += pow((float(x[i])-float(xi[i])),2)
     d = math.sqrt(d)
     return d


# In[5]:


#knn prediction
def knn_predict(test_data, train_data, k_value):
    for i in test_data:
        eu_Distance =[]
        knn = []
        normal = 0                             #change according to classification
        mild = 0
        moderate = 0
        severe = 0
        vsevere = 0
        for j in train_data:
            eu_dist = euclideanDist(i, j)
            eu_Distance.append((j[1], eu_dist))  #change feature column
            eu_Distance.sort(key = operator.itemgetter(1))
            knn = eu_Distance[:k_value]
            for k in knn:                       #change according to classification
                if k[0] =='NORMAL':
                    normal += 1
                if k[0] =='MILD':
                    mild += 1
                if k[0] =='MODERATE':
                    moderate += 1
                if k[0] =='SEVERE':
                    severe += 1
                if k[0] =='VERY SEVERE':
                    vsevere += 1
        
        if normal > mild and normal > moderate and normal > severe and normal > vsevere:
            i.append('NORMAL')
        elif mild > normal and mild > moderate and mild > severe and mild > vsevere:
            i.append('MILD')
        elif moderate > normal and moderate > mild and moderate > severe and moderate > vsevere:
            i.append('MODERATE')
        elif severe > normal and severe > mild and severe > moderate and severe > vsevere:
            i.append('SEVERE')
        else:
            i.append('VERY SEVERE')
       


# In[6]:


#Accuracy calculation function
def accuracy(test_data):
    correct = 0
    for i in test_data:
        if i[1] == i[2]:                           #change feature nd label column
            correct += 1
    accuracy = float(correct)/len(test_data) *100  #accuracy 
    return accuracy


# In[7]:


data = getdata("D:\\2.csv")  #load csv file as parameter
train_dataset, test_dataset = shuffle(data) #train test data split
K = 15                                         # Assumed K value . K =n^(1/2)
knn_predict(test_dataset, train_dataset, K)   
print test_dataset
print "Accuracy : ",accuracy(test_dataset)
print len(test_dataset)


# In[2]:


get_ipython().magic(u'R print(ggplot(aes(x=FEV1, y=FEV1(predicted), color=COPD) + geom_point())')


# In[9]:


get_ipython().magic(u'R print(ggplot(data=df) + geom_point(aes(x=A, y=B, color=C)))')

