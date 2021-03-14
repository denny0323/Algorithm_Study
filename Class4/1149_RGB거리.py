#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
> Problem
@ 백준 Class4 1149번
@ RGB거리
@ URL https://www.acmicpc.net/problem/1149
'''

import sys
input = sys.stdin.readline

N = int(input())
RGBprices = {}
for i in range(N):
    RGBprices[i+1] = list(map(int, input().split()))
    
prices = [0]*(N+1)
colors = [-1]*(N+1)

def RGB(i):
    if i == 2:
        price_i = RGBprices[i-1]
        price_i1 = RGBprices[i]
        if min(price_i) < min(price_i1):
            prices[i-1] = min(price_i)  # price
            color_i = price_i.index(min(price_i)) # color
            colors[i-1] = color_i

            price_i1[color_i] = 1001

            prices[i] = min(price_i1)
            color_i1 = price_i1.index(prices[i]) 
            colors[i] = color_i1
        else:
            prices[i] = min(price_i1)  # price
            color_i1 = price_i1.index(min(price_i1)) # color
            colors[i] = color_i1

            price_i[color_i1] = 1001

            prices[i-1] = min(price_i)
            color_i = price_i.index(prices[i-1]) 
            colors[i-1] = color_i
        return sum(prices[:3])
    else:
        color_i_1 = colors[i-1]
        RGBprices[i][color_i_1] = 1001
        prices[i] = min(RGBprices[i])
        return RGB(i-1) + prices[i]
print(RGB(N))

'''
> result : 틀렸습니다.
: 처음의 최소가 항상 최소가 아님. 
> solution : 각 R, G, B로 시작했을때를 모두 구해서 그 중 최소인 case를 출력해야함
'''

import sys
input = sys.stdin.readline

N = int(input())
prices = []
for i in range(N):
    prices.append(list(map(int, input().split())))
    
for i in range(1, len(prices)):
    prices[i][0] += min(prices[i-1][1], prices[i-1][2])
    prices[i][1] += min(prices[i-1][2], prices[i-1][0])
    prices[i][2] += min(prices[i-1][0], prices[i-1][1])
print(min(prices[N-1]))

'''
> result 
@ Memory : 29028 KB
@ Time : 64 ms
@ Code length : 403 B
'''

