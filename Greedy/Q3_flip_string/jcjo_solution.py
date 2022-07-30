#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#link: https://www.acmicpc.net/problem/1439
#memory: 30840KB
#time: 	76ms


# In[1]:


data = '0001100'


# In[6]:


#맨 첫 번째는 별도로 세주자.
if data[0] == '0':
    count0 = 0 #전체를 0으로 뒤집을 때, 필요한 횟수
    count1 = 1 #전체를 1으로 뒤집을 때, 필요한 횟수
else:
    count0 = 1
    count1 = 0
print(count0, count1)


# In[7]:


for idx in range(len(data)-1):
    if (data[idx] == '0') and (data[idx+1] == '1'):
        count0 += 1
    elif (data[idx] == '1') and (data[idx+1] == '0'):
        count1 += 1

print(f"count0:{count0}, count1:{count1}, 따라서 최솟값은 {min(count0, count1)}")

