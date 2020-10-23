#!/usr/bin/env python
# coding: utf-8

# In[1]:


def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))


# In[23]:


def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
print(ack(3,4))
print(ack(4,5))


# In[31]:


def first(word):
    return word[0] 

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome('apple'))
print(is_palindrome('think'))
print(is_palindrome('Python'))
print(is_palindrome('abba'))
print(is_palindrome('abbba'))
print(is_palindrome('aaaaaa'))


# In[39]:


def is_power(a,b):
    if a%b==0:
        if a/b==1:
            return True
        else:
            return is_power(a/b,b)
    else:
        return False

print(is_power(8,2))
print(is_power(6,2))
print(is_power(125,5))
print(is_power(35,5))
print(is_power(1024,2))
print(is_power(1000,10))


# In[ ]:




