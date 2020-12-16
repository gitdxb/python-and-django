#!/usr/bin/env python
# coding: utf-8

# In[1]:


def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)


# In[3]:


def spam():
    eggs = 'spam local'
    print(eggs)
    
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs)


# In[4]:


def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)


# In[6]:


def spam():
    global eggs
    eggs = 'spam'
def bacon():
    eggs = 'bacon'
def ham():
    print(eggs)
eggs = 42
spam()
bacon()
ham()
print(eggs)


# In[10]:


def spam(number):
    try:
        return 42 / number
    except ZeroDivisionError:
        print('Invalid number')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


# In[ ]:




