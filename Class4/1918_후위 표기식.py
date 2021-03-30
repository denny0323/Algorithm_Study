'''
> Problem
@ 백준 Class4 1918번
@ 후위 표기식
@ URL https://www.acmicpc.net/problem/1918
'''
 
Infix = input()

def InfixToPostfix(Infix):
    stack = []
    res = ''  # list로하니 메모리 초과
    order = {'*':2, '/':2, '+':1, '-':1, '(':0}

    for curr in Infix:   
        if curr.isalpha() :
            res += curr
        
        elif curr == '(':
            stack.append(curr)
        
        elif curr == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop() # '(' 꺼내기
    
        else: ## 연산자
            while stack and order[curr] <= order[stack[-1]]:
                res += stack.pop()
            stack.append(curr)

    while stack:
        res += stack.pop()
    return res
   
print(InfixToPostfix(Infix))

'''
> result 
@ Memory : 28776 KB
@ Time : 68 ms
@ Code length : 704 B
'''
