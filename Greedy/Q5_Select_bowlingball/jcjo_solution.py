#!/usr/bin/env python
# coding: utf-8

# In[48]:


n = 5
m = 3
bball = [1, 3, 2, 3, 2]


# In[52]:


n = 8
m = 5
bball = [1, 5, 4, 3, 2, 4, 5, 2]


# In[53]:


from itertools import combinations


# In[54]:


len([i for i in combinations(bball, 2) if i[0] != i[1]])


# In[55]:


"""
답안 연습
"""

#두 명, 서로 다른 공, 같은 무게도 번호로 구별, 조합(순서 고려 안함)

#번호 별 개수

count_list = [0] * 11 #인덱스는 0부터 시작하므로 10(문제 조건)+1개
for b in bball:
    count_list[b] += 1

result = 0
for i in range(1, m+1):
    n -= count_list[i] 
    result += count_list[i] * n
result        

#하나를 선택하고 나머지 선택하고 - 단, 순열과 달리 나머지가 처음이 아닌 나머지가 아니라
#처음 뽑은 것과도 다르되, 이전 선택과도 달라야 한다. 예를 들어 1 - 2,3/ 2 - 3/ 3 - None(조합)


# In[ ]:


"""
lambda & list_comprehension

1. lambda x: return1 if1 _ else return2
2. list_comprehesion: [return1 for _ in if _]
                      [return1 if_ else return2 for _ in ]
                      
# 이보다 길어지는 경우는 사용자 함수로 정의해서 쓰자!                      
"""

