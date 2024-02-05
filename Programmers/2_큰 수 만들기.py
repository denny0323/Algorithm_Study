from itertools import combinations

number = "1924"; k = 2
number = "1231234"; k = 3
number = "4177252841"; k = 4

# 조합 (정확성 33.3)
# N = len(number)
# max_num = 0
# for mask in combinations(list(range(N)), N-k):
#      num = ''.join(x for x in list(map(number.__getitem__, mask)))
#      max_num = max(int(num), max_num)
#
# print(str(max_num))

# stack

def solution(number, k):
     stack = []
     for num in number:
          if not stack:
               stack.append(num)
               continue
          if k > 0:
               while stack[-1] < num:
                    stack.pop()
                    k -= 1
                    if not stack or k <= 0:
                         break
          stack.append(num)
     stack = stack[:-k] if k > 0 else stack
     return ''.join(stack)


def solution(number, k):
     answer = []  # Stack

     for num in number:
          while k > 0 and answer and answer[-1] < num:
               answer.pop()
               k -= 1
          answer.append(num)

     return ''.join(answer[:len(answer) - k])