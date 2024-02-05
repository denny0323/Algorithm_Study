'''
> Problem
@ 백준 문제집 <단기간 성장> 14725번
@ 개미굴
@ URL https://www.acmicpc.net/problem/14725
'''
import sys
sys.stdin=open("./input/14725.txt", "r")
input = sys.stdin.readline

N = int(input())

'''
    Ditionary 이용
    @ source: https://velog.io/@jini_eun/%EB%B0%B1%EC%A4%80-14725%EB%B2%88-%EA%B0%9C%EB%AF%B8%EA%B5%B4-Java-Python
'''
# anthill = {}
#
# for _ in range(N):
#     info = list(input().split())
#     scope = anthill
#     for j in info[1:]:
#         if j not in scope:
#             scope[j] = {}
#         scope = scope[j]
#
# print(anthill)
#
# DFS print
# def getResult(k, i):
#     scope_key = sorted(k.keys())
#     for s in scope_key:
#         print('--'*i + s)
#         getResult(k[s],i+1)
#
# getResult(anthill, 0)

'''
    Trie 구조
    @ soucre: https://dreamtreeits.tistory.com/35
'''
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
        cur_node = self.root
        for c in s:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node['*'] = {}

    def print_trie(self, l, cur_node=None):
        if l == 0:
            cur_node = self.root

        for c in sorted(cur_node.keys()):
            if c != '*':
                print('--' * l, c, sep="")
            self.print_trie(l + 1, cur_node[c])


trie = Trie()
for _ in range(N):
    data = list(input().split())
    trie.insert(data[1:])

trie.print_trie(0)