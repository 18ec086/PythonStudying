#!/usr/bin/env python
# coding: utf-8

# In[35]:


fin =open("words.txt")
dictionary=dict()

def create():
    cnt=0
    for line in fin:
        word=line.strip()
        dictionary[word]=cnt
        cnt+=1
    return dictionary

def isExisted(str):
    print(str in dictionary or str in dictionary.values())
create()
isExisted("aa")
isExisted("aaaa")
isExisted(100)
isExisted(1)
isExisted(11111111)
isExisted("abbesses")
isExisted(500)
isExisted("zymurgy")


# In[44]:


def histogram(s):
    d =dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d
def invert_dict(s):
    a={}
    for key in s:
        b=s[key]
        a.setdefault(b, []).append(key)
    return a

hist =histogram("parrot")
inverse =invert_dict(hist)
inverse


# In[52]:


d={}
def ack(m,n):
    if m==0:
        return n+1
    if n==0:
        return ack(m-1,1)
    try:
        return d[m,n]
    except KeyError:
        d[m,n]=ack(m-1,ack(m,n-1))
    return d[m,n]

print(ack(3,4))


# In[158]:


def has_duplicates(d):
    return len(set(d))!=len(d)
print(has_duplicates([1,2,3]))
print(has_duplicates([1,2,2,3]))
print(has_duplicates([1,2,3,3]))
print(has_duplicates([1,2,3,4]))
print("----")
print(has_duplicates(["a","b","c","d"]))
print(has_duplicates(["a","b","b","d"]))
print(has_duplicates(["a","b","c","c"]))
print(has_duplicates(["a","b","c","d"]))


# In[ ]:




