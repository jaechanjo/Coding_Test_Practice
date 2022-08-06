#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#link: https://www.acmicpc.net/problem/18406
#memory: 30840KB
#time: 76ms


# In[2]:


n = '123402'
n2 = '7755'


# In[16]:


med = int(len(n) / 2) #항상 짝수 개 자릿수의 n이므로 그냥 나누기만 해도 괜찮다.

if sum([int(i) for i in n[:med]]) == sum([int(i) for i in n[med:]]): #왼쪽 n/2개의 합과 오른쪽 n/2개의 합이 같은지 확인
    print("LUCKY")
else:
    print("READY")

