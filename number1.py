
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[19]:


x = np.random.randint(30,size=20)
y = np.random.randint(40,size=20)


# In[20]:


# some edits in edits branch
y = np.exp(y)


# In[21]:


y = np.power(y,0.1)


# In[22]:


y


# In[23]:


x


# In[24]:


plt.scatter(x,y)


# This is a random plot but I changed y values
