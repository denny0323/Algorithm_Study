'''
> Problem
@ 백준 Class4 1043번
@ 거짓말
@ URL https://www.acmicpc.net/problem/1043
'''


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_T = list(map(int, input().split()))
T = set(num_T[1:])

meet = {i:set() for i in range(1, N+1)}
parties = []
for i in range(M):
    party = list(map(int, input().split()))[1:]
    for j in range(len(party)):
        meet[party[j]] = meet[party[j]].union(set(party[:j] + party[j+1:])) 
    
    set_party = set(party)
    parties.append(set_party)
    if len(set_party.intersection(T)) > 0:
        T = T.union(set_party)
        
cnt = 0
for party in parties:
    if len(party.intersection(T)) == 0:
        cnt += 1

print(cnt)

'''
> result : 틀렸습니다.
> viral을 고려안함. 1->2->3 일때, 1->3까지 전달이 안된다고 구현.
> solution : T를 update할때, 각 party를 확인하면서 모든 party list를 다시 검토해야 viral을 잡을 수 있음
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = set(input().split()[1:])

checker = [0] * M
parties = []

for i in range(M):
    parties.append(set(input().split()[1:]))

for _ in range(M):
    for i, party in enumerate(parties):
        if len(T.intersection(party)) == 0:
            checker[i] = 1
        else:
            checker[i] = 0
            T = T.union(party)
print(sum(checker))
'''
> result 
@ Memory : 28776 KB
@ Time : 96 ms
@ Code length : 420 B
'''

