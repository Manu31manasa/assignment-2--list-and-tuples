#!/usr/bin/env python
# coding: utf-8

# # write a python program to get a list, sortes in increasing order by the last element in each tuple from a given list of non-empty tuples

# In[3]:


x = [(2 , 5), (1 , 2), (4 , 4), (2 , 3), (2 , 1)]
y = sorted(x)
pos0 = 0
pos1 = 1
pos3 = 3
pos4 = 4
y[pos0],y[pos1] = y[pos1],y[pos0]
y[pos3],y[pos4] = y[pos4],y[pos3]
print(y)


# In[ ]:




