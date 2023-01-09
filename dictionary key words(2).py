#!/usr/bin/env python
# coding: utf-8

# # write a python program to print a dictionary whose key words should be tha alphabet from a - z and the value should be corresponding ASCII values 

# In[1]:


x = input("enter a character is: ")
dict = {}
for x in range(ord('a'),ord('z')+1):
    dict[chr(x)] = x
print(dict , end = " ")


# In[ ]:




