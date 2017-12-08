
# coding: utf-8

# In[16]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[17]:


x = np.random.randint(40,size=20)
y = np.random.randint(30,size=20)


# In[18]:


# some more changes in master
y = np.power(y**0.5,3)


# In[19]:


y = np.power(y,4)


# In[20]:


y


# In[21]:


x


# In[22]:


plt.scatter(x,y)


# This is a random plot but I changed y values
