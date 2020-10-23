#!/usr/bin/env python
# coding: utf-8

# In[2]:


def nested_sum(t):
    total =0
    for i in t:
        total+=sum(i)
    return total

t=[[1,2],[3],[4,5,6]]
nested_sum(t)


# In[4]:


def cumsum(t):
    total=0
    a =[]
    for x in t:
        total+=x
        a.append(total)
    return a
t=[1,2,3]
cumsum(t)


# In[5]:


def middle(t):
    return t[1:-1]
t=[1,2,3,4]
middle(t)


# In[7]:


def chop(t):
    del t[0]
    del t[-1]
t=[1,2,3,4]
chop(t)
t


# In[ ]:




