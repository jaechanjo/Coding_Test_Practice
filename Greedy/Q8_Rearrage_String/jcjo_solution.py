#!/usr/bin/env python
# coding: utf-8
# %%
#jcjo_solution

data = 'K1KA5CB7'
data2 = 'AJKDLSI412K4JSJ9D'


# %%


num_set = {str(n) for n in range(10)} #숫자가 0~9까지 검증용 집합

result = ''
num_sum = 0
str_list = []

#split str, num
for s in data2:
    
    if s not in num_set: #숫자인지 문자인지 확인
        str_list.append(s) #문자이면 따로 리스트에 모으자
    else:
        num_sum += int(s) #숫자이면 더하자

str_sorted = sorted(str_list) #문자 리스트를 정렬(아스키 코드 순)
if num_sum != 0:
    str_sorted.append(str(num_sum)) #0이 아니면, 숫자 합을 문자로 끝에 추가

for r in str_sorted: #최종적으로 다 붙여주자.
    result += r

result


# %%


# 답안 복습 - char.isdigit()/ char.isalpha() - 아스키 코드 중 숫자에 해당하는 구간인지 문자에 해당하는 구간인지 판별해주는 메서드
#           - ''.join(list): 리스트를 문자열을 한 번에 이어주는 메서드

result = []
value = 0

for s in data2:
    
    if s.isdigit():
        value += int(s)
    else:
        result.append(s)
        
result.sort()

if value != 0:
    result.append(str(value))
    
print(''.join(result))

