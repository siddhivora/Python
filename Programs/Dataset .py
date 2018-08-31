
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[25]:


lim=100
X = ['MILD','MODERATE','SEVERE','VERY SEVERE','NORMAL']

df=pd.DataFrame({'AGE':[np.random.randint(40,80) for i in range (lim)]})
df['SEX']=[np.where(df.iloc[i,0]%2==0,'MALE','FEMALE') for i in range (lim)]
df['HEIGHT']=[np.random.randint(150,220) for i in range (lim)]
df['WEIGHT']=[np.random.randint(60,100) for i in range (lim)]
df['FEV1']=[np.random.uniform(0.4,4.5) for i in range (lim)]
df['FVC']=[np.random.uniform(1.1,12.2) for i in range (lim)]
df['FEV1(predicted)']=0
df['FVC(p)']=0
df['%FEV1pred']=0
df['rCOPD']=X[0]


# In[26]:


for i in range(len(df)):
    #FEV1 & FVC predicted
    if df.iloc[i,1]==['MALE']:
        df.iloc[i,6]=-3.682-0.024*df.iloc[i,0]+0.046*df.iloc[i,2]
        df.iloc[i,7]=-5.048-0.014*df.iloc[i,0]+0.054*df.iloc[i,2]+0.006*df.iloc[i,3]
    if df.iloc[i,1]==['FEMALE']:
        df.iloc[i,6]=-2.267-0.019*df.iloc[i,0]+0.033*df.iloc[i,2]
        df.iloc[i,7]=20.07-0.010*df.iloc[i,0]-0.261*df.iloc[i,2]+0.000972*df.iloc[i,2]*df.iloc[i,2]
    #calculation for % FEV1 Predicted
    df.iloc[i,8]=((df.iloc[i,4]*100)/df.iloc[i,6])
    #print(df.iloc[i,0])
    if df.iloc[i,4]>0.8*df.iloc[i,6] and df.iloc[i,4]<df.iloc[i,6]:
        df.iloc[i,9]=X[0]
    if df.iloc[i,4]>0.5*df.iloc[i,6] and df.iloc[i,4]<0.8*df.iloc[i,6]:
        df.iloc[i,9]=X[1]
    if df.iloc[i,4]>0.3*df.iloc[i,6] and df.iloc[i,4]<0.5*df.iloc[i,6]:
        df.iloc[i,9]=X[2]
    if df.iloc[i,4]<0.3*df.iloc[i,6]:
        df.iloc[i,9]=X[3]
    if df.iloc[i,4]>df.iloc[i,6]:
        df.iloc[i,9]=X[4]
df.to_csv("D:/1.csv",index=False)


# In[36]:


df1=pd.DataFrame((df.iloc[:,8]),(df.iloc[:,9]))
df1.to_csv("D:\\2.csv",index=False)


# In[ ]:


colNums = [8, 9]
to_write = [ col for i, col in enumerate(zip(*my_reader)) if i in colNums ]

