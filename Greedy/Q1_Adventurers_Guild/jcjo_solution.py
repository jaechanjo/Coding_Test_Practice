#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = 5
fear = [2, 3, 1, 2, 2]


# In[5]:


fear.sort(reverse = True)
fear


# In[9]:


# fear: 공포도 list
# start: 공포도 list 시작 index
# count: 그룹을 구성한 횟수

def grouping(start, fear, count):
    if start >= n:
        print(count)
    else:
        count += 1 #그룹을 구성
        start += fear[start] #옮겨진 index 만큼 모험가 그룹에 인원이 추가됐다고 생각한다.
        
        grouping(start=start, fear=fear, count=count)


# In[10]:


grouping(start=0, fear=fear, count=0)

