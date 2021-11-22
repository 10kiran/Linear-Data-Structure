#!/usr/bin/env python
# coding: utf-8

# In[1]:


class elements:
  def twoSum(self, nums, target):
       lookup = {}
       for i, num in enumerate(nums):
           if target - num in lookup:
               return (lookup[target - num], i )
           lookup[num] = i
print("number1=%d, number2=%d" % elements().twoSum((10,20,10,40,50,60,70),50))


# In[ ]:




