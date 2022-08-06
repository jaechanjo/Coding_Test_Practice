#!/usr/bin/env python
# coding: utf-8

# In[27]:


food_times = [3, 1, 2] #음식 섭취 남은 시간
k = 5 #5초 후에 네트워크 장애


# In[28]:


"""
답안 공부
"""

#최소 음식 시간부터 해치우자. 그렇게 성큼성큼 걸어 순식간에 도달하자.
#오름차순 정렬 및 음식 번호 태깅 -> 우선순위 큐(최소힙) : heapq

import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    #먹기 위해 사용한 시간    
    sum_eat_time = 0    
    #이전 음식 시간
    previous = 0
    #음식 개수    
    length = len(food_times)
    
    while sum_eat_time + (q[0][0] - previous) * length < k:
        now = heapq.heappop(q)[0]
        sum_eat_time = (now - previous) * length
        length -= 1
        previous = now
    
    result = sorted(q, key=lambda x: x[1])
    
    return result[(k - sum_eat_time) % length][1]


# In[29]:


solution(food_times, k)


# In[24]:


# 2th-fail
# sec = 0
# i = 0
# while True:
#     i = i % 3
    
#     if sec == k:
#         result = i+1
#         break
    
#     if food_times[i] == 0:
        
#         if sum(food_times) == 0:
#             result = -1
    
#     else:
#         food_times[i] -= 1
#         sec += 1
        
#     i +=1

# result


# In[10]:


# 1st-fail

# def recursive(i):
    
#     if food_times[i] == 0:
        
#         if sum(food_times) == 0:
#             return -1, i
#         else:
#             if food_times[(i+1)%3] == 0:
#                 recursive(i=(i+1)%3)
#             else:
#                 food_times[(i+1)%3] -= 1
#     else:
#         food_times[i] -= 1
    
#     return food_times, i


# In[11]:


# def solution(food_times, k):

#     sec = 0
#     i = 0
#     while True:

#         food_times, i = recursive(i)

#         if food_times == -1:
#             result = i+1
#             break
#         else:
#             i = (i + 1)%3
#             sec += 1
#     return result

