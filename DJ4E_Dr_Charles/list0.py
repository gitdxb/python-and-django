#!/usr/bin/env python
# coding: utf-8

# In[11]:


numberOfCat = int(input('How many cats do you own? =>...'))
catList = []
print("Tell me name of each cat: ")
for i in range(numberOfCat):
    print('Cat name ', i+1, ': ', end='')
    cat = input()
    catList.append(cat)

print('So you have: ')
for i in catList:
    print(i, end=' ')


# In[13]:


supplies =['pen', 'staplers', 'flamethrowners', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index + 1) + ' in supplies is: ' + item)


# In[ ]:




