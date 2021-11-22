#!/usr/bin/env python
# coding: utf-8

# In[32]:


def smallest(numbers):
    m1 = m2 = float('inf')
    for x in numbers:
        if x < m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m1
print(smallest([5, 2, 3, 4]))


# In[ ]:




