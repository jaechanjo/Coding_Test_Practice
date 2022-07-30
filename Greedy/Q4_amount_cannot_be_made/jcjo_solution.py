#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = 5
coin = [3, 2, 1, 1, 9]


# In[13]:


from itertools import combinations
can_made = list({sum(j) for i in range(1, n+1) for j in combinations(coin, i)}) #만들 수 있는 금액 합계
can_made


# In[16]:


max(can_made)


# In[18]:


for idx in range(max(can_made)):
    if can_made[idx+1] == can_made[idx] + 1: #연속적인 숫자 나열 중 빠진 부분, 즉 만들 수 없는 최솟값
        pass
    else:
        result = can_made[idx] + 1
        break
result


# In[ ]:


#시간 복잡도가 조금.. 비싸긴 하다. 그러나 이런 방법도 있다는 차원.


# In[19]:


#답지 복습: 
#Key-Idea: target 보다 작거나 같은 수가 있다면 만들 수 있고, target에 그 수를 더한 값 -1 까지 만들 수 있다.

target =1 #동전의 최솟값은 1

coin.sort() #오름차순 정렬해서, 작은 수부터 차례대로 뽑기만 하면 되도록 하자.

for i in coin:
    if i <= target:
        target += i #target보다 작은 값만큼 만들 수 있는 범위 확장, 이 값부터 다시 확인.
    else:
        result = target
        break
result

