#!/usr/bin/env python
# coding: utf-8

# In[15]:


import math

def mysqrt(a):
    x=a/2
    while True:
        y=(x+a/x)/2
        if x==y:
            break
        x=y
    return x

def test_square_root():
    str1 = "a"
    str2 ="mysqrt(a)"
    str3="math.sqrt(a)"
    str4="diff"
    
    line1="-"
    line2="---------"
    line3="------------"
    line4="----"
    
    space2=" "*3
    space3=""
    print(str1,str2,space2,str3,space3,str4)
    print(line1,line2,space2,line3,space3,line4)
    for a in range(1,10):
        cal1=mysqrt(a)
        cal2=math.sqrt(a)
        cal3=abs(cal1-cal2)
        print(a,"{:<13f}".format(cal1),"{:<13f}".format(cal2),cal3)
    
test_square_root()


# In[19]:


import math
def eval_loop():
    result =None
    while True:
        str=input("文字列を入力")
        if str=="done":
            break
        else:
            y=eval(str)
            print(y)
    return y
eval_loop()


# In[33]:


import math
def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
    
def estimate_pi():
    sum=0
    x=0
    k=0
    c=2*math.sqrt(2)/9801
    while True:
        x=fac(4*k)*(1103+26590*k)/(fac(k)**4 * 4396**(4*k))
        if x<1e-15:
            break
        sum+=x
        k+=1
    return 1/(c*sum)
print(estimate_pi())
print(math.pi)


# In[ ]:




