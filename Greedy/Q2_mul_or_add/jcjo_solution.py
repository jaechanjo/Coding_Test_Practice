#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = '02984'
data2 = '567'


# In[15]:


len(data)


# In[16]:


result = int(data[0]) #연산 결과, 시작은 첫 번째 index 부터
result


# In[17]:


for idx in range(len(data)-1):
    if (data[idx] in ['0', '1']) | (data[idx+1] in ['0', '1']): #0또는 1이면 더하기가 이득.
        result += int(data[idx+1])
    else: # 그 외에는, 항상 곱하기가 이득
        result *= int(data[idx+1])
result        

