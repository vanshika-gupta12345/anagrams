#!/usr/bin/env python
# coding: utf-8

# In[1]:


a="boat"
print(a)
b=list(a)
print(b)
b[0],b[2]=b[2],b[0]
print(b)
word=""
d=word.join(b)
print(d)


# In[2]:


a="boat"
b=list(a)
print(b)
def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
c=swap(b,0,2)
word=""
d=word.join(c)
print(d)


# In[3]:


m="checkmate"
n=list(m)
print(n)
def swap(list,pos1,pos2,pos3):
    list[pos1],list[pos2],list[pos3]=list[pos3],list[pos1],list[pos2]
    return list
y=swap(n,1,4,7)
z=""
t=z.join(y)
print(t)


# In[4]:


a="vanshika"
print(a)
b=list(a)
b[0],b[1],b[2],b[3]=b[2],b[3],b[1],b[0]
c=""
d=c.join(b)
print(d)


# In[5]:


a='tente'
print(a)
b=list(a)
def swap(b,pos1,pos2):
    b[pos1],b[pos2]=b[pos2],b[pos1]
    return b
f=swap(b,3,4)
d=""
e=d.join(f)
print(e)


# In[ ]:




