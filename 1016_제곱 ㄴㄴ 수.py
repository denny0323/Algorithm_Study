#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
> Problem
@ 백준 Class4 1016번
@ 제곱 ㄴㄴ 수
@ URL https://www.acmicpc.net/problem/1016
'''


# In[54]:


# input_file = open('./input/1016.txt', 'r')
# input = input_file.readline


# In[ ]:


# import sys
# from collections import deque
# input = sys.stdin.readline


# * 에라토스테네스의 체 (소수 판별 알고리즘)  
#     : 1이상의 자연수의 배수를 다 지워가며 판별함 (자기 자신은 제외)

# In[22]:


import math

min, max = map(int, input().split())
cnt = max-min+1
max_rt = int(math.sqrt(max))
checker = [1] * cnt

idx = 0
for i in range(min, max+1):
    for j in range(2, max_rt+1):
        sq_num = j**2
        if checker[idx] > 0 and i % sq_num == 0: # 첫방문임 + 제곱수임
            checker[idx] = 0
    idx += 1
print(sum(checker))


# In[ ]:


'''
> result : 시간초과
'''


# In[30]:


import math

min, max = map(int, input().split())
cnt = max-min+1
max_rt = int(math.sqrt(max))
checker = [1] * cnt

squres = [j**2 for j in range(2, max_rt+1)]
for sq_num in squres:
    # 최고 제곱수의 배수와의 차이이자, index
    cur = (math.ceil(min/sq_num)*sq_num)-min     ## min // sq_num 쓰면 안됨. 분수의 경우, 1이 나와야함.
    # index가 넘지 않을 동안
    while cur <= max - min:
        checker[cur] = 0
        cur += sq_num

print(sum(checker))


# In[ ]:


'''
> result 
@ Memory : 78700 KB
@ Time : 924 ms
@ Code length : 322 B
'''

