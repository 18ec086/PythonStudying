#!/usr/bin/env python
# coding: utf-8

# In[17]:


import time
d= time.time()
seconds=d%60
minutes=(d//60)%60
hours=(d//3600)%24
days=d//(3600*24)
print("時間:"+str(hours)+", 分:"+str(minutes)+", 秒:"+str(seconds)+", 経過日数:"+str(days))


# In[ ]:





# In[ ]:


def check_fermat(a,b,c,n):
    if n>2 and (a**n+b**n==c*n):
         print("Holy smokes,Fermat was wrong!")
    else:
        print("No,that doesn't work")
            
check_fermat(2,3,4,5)
print("aaa")


# In[ ]:





# In[ ]:




