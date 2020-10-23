#!/usr/bin/env python
# coding: utf-8

# In[31]:


def reverse(s):
    t=s.split("-")
    t.sort()
    t='-'.join(t)
    return t

s="green-red-yellow-black-white"
reverse(s)


# In[32]:


def addValue(d1,d2):
    d={}
    d.update(d1)
    d.update(d2)
    s=list(d.keys())
    for i in s:
        try:
            d[i]=d1[i]+d2[i]
        except KeyError: 
            pass
    return d
    
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 400, 'd': 200}
print(addValue(d1,d2))
print(d1)
print(d2)


# In[68]:


def flatten_list(n_list):
    l=[]
    for x in n_list:
        if isinstance(x,list):
            l+=flatten_list(x)
        else:
            l.append(x)
    return l

s=[0, 10, [20, 30], 40, 50, [60, 70, 80], [[90, 100], 110, 120]]
print(flatten_list(s))


# In[147]:


def is_palindrome(s,t):
    return s[::-1]==t

def check(son,mom):
    if son<10:
        s="0"+str(son)
    else:
        s=str(son)
    return is_palindrome(s,str(mom))

def cntTimes(age,dif):
    cnt=0
    for c in range(age+1):
        if c+dif>99:
            break
        if check(c,c+dif):
            cnt+=1
    return cnt


def solution():
    max=99
    for son in range(max):
        for dif in range(18,max,9):
            if cntTimes(max,dif)==8 and cntTimes(son,dif)==6:
                return son
            
        
print(str(solution())+"歳")


# In[ ]:




