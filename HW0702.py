#!/usr/bin/env python
# coding: utf-8

# In[7]:


str="banana"
print(str.find("123"))
print(str.find("na"))
print(str.find("ba"))
print(str.find("an"))
print(str.find("apple"))
print("--------")
str="Think Python"
print(str.find("123"))
print(str.find("Think"))
print(str.find("think"))
print(str.find("nk"))
print(str.find("Py"))
print(str.find("apple"))


# In[11]:


str ="   Think    "
print(str.strip())
print(str.strip("xxx"))
print(str.strip("Tk"))
print(str.strip("k"))
print(str.strip("T"))
print("-------")
str="TTTThinkkkk"
print(str.strip())
print(str.strip("xxx"))
print(str.strip("Tk"))
print(str.strip("k"))
print(str.strip("T"))


# In[13]:


str="aaaaabbbbbbcccccc"
print(str.replace("a","x"))
print(str.replace("a","x",3))
print(str.replace("a","zz"))
print(str.replace("a",""))
print(str.replace("b","zzz",3))
print(str.replace("n","zz"))


# In[16]:


str="banana"
str.count("a")


# In[30]:


def is_palindrome(str):
    return True if str==str[::-1] else  False

print(is_palindrome("noon"))
print(is_palindrome("qwert"))
print(is_palindrome("redivider"))
print(is_palindrome("abcbca"))
print(is_palindrome("abcbcba"))


# In[51]:


def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
    
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True

print(any_lowercase1("abccDDEE"))
print(any_lowercase1("DDEE"))
print(any_lowercase1("DDEEabcc"))
print(any_lowercase1("abcc"))
print("----------")
print(any_lowercase2("abccDDEE"))
print(any_lowercase2("DDEE"))
print(any_lowercase2("DDEEabcc"))
print(any_lowercase2("abcc"))
print("----------")
print(any_lowercase3("abccDDEE"))
print(any_lowercase3("DDEE"))
print(any_lowercase3("DDEEabcc"))
print(any_lowercase3("abcc"))
print("----------")
print(any_lowercase4("abccDDEE"))
print(any_lowercase4("DDEE"))
print(any_lowercase4("DDEEabcc"))
print(any_lowercase4("abcc"))
print(any_lowercase4("Tt"))
print(any_lowercase4("AAQWsweRFTG"))
print("----------")
print(any_lowercase5("abccDDEE"))
print(any_lowercase5("DDEE"))
print(any_lowercase5("DDEEabcc"))
print(any_lowercase5("abcc"))
print(any_lowercase5("Tt"))
print(any_lowercase5("AAQWsweRFTG"))


# In[ ]:




