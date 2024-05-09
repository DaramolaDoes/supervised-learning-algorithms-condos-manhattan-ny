#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd


# In[5]:


#importing csv and defining columns
df = pd.read_csv('Desktop/Manhattan/manhattandd.csv')


# In[6]:


#view data
df


# In[7]:


import statsmodels.api as sm


# In[9]:


#define response variable
y = df['Price']


# In[10]:


#define predictor variables
x = df['Date']


# In[11]:


#add constant to predictor variables
x = sm.add_constant(x)


# In[12]:


#fit linear regression model
model = sm.OLS(y, x).fit()


# In[13]:


#view model summary
print(model.summary())


# In[14]:


-1.899e+08 + 949.3865*(202403)


# In[15]:


-1.899e+08 + 949.3865*(202404)


# In[16]:


-1.899e+08 + 949.3865*(202405)


# In[17]:


-1.899e+08 + 949.3865*(202406)


# In[18]:


-1.899e+08 + 949.3865*(202407)


# In[19]:


-1.899e+08 + 949.3865*(202408)


# In[20]:


-1.899e+08 + 949.3865*(202905)


# In[21]:


-1.899e+08 + 949.3865*(203405)


# In[22]:


-1.899e+08 + 949.3865*(205405)


# In[ ]:




