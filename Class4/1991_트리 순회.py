'''
> Problem
@ 백준 Class4 1991번
@ 트리 순회
@ URL https://www.acmicpc.net/problem/1991
'''


# import sys
# input = sys.stdin.readline
# input_file = open('./input/1991.txt', 'r')
# input = input_file.readline

N = int(input())
tree = {}
for _ in range(N):
    p, l_c, r_c = input().split()
    tree[p] = (l_c, r_c)

def preorder():
    stack = []
    stack.append('A')
    res = ''
    
    while stack:
        curr = stack.pop()
        res += curr
        l_c, r_c = tree[curr]
        
        if r_c != '.':
            stack.append(r_c)
        if l_c != '.':
            stack.append(l_c)
    return res

def inorder():    
    curr = 'A'
    res, stack = [], []
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = tree[curr][0] if tree[curr][0] != '.' else False
        else:
            curr = stack.pop()
            res.append(curr)
            curr = tree[curr][1] if tree[curr][1] != '.' else False
    return res

def postorder():
    stack = ['A']
    res = ''
    
    while stack:
        if tree[stack[-1]][0] != '.' and tree[stack[-1]][0] not in res:
            stack.append(tree[stack[-1]][0])
            
        elif tree[stack[-1]][1] == '.' or tree[stack[-1]][1] in res:
            res += stack.pop()
            
        else:
            stack.append(tree[stack[-1]][1])
    return res

print(preorder())
print(*inorder(), sep='')
print(postorder())


'''
> result 
@ Memory : 28776 KB
@ Time : 64 ms
@ Code length : 1216 B
'''


### 재귀 이용
### source: https://suri78.tistory.com/134
import sys 
sys.setrecursionlimit(10**6) 

def preorder(node): 
	if node == '.': 
		return 
	print(node, end = "") 
	preorder(tree[node][0]) 
	preorder(tree[node][1]) 
	
def inorder(node): 
	if node == '.': 
		return 
	inorder(tree[node][0]) 
	print(node, end = "") 
	inorder(tree[node][1]) 
	
def postorder(node): 
	if node == '.': 
		return 
	postorder(tree[node][0]) 
	postorder(tree[node][1]) 
	print(node, end = "") 
	
n = int(input()) 
tree = {} # make tree 
for _ in range(n): 
	root, left, right = input().split()
	tree[root] = (left, right)

preorder('A') 
print() 
inorder('A') 
print() 
postorder('A')

'''
> result 
@ Memory : 28776 KB
@ Time : 72 ms
@ Code length : 668 B
'''

