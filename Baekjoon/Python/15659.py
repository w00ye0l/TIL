from itertools import permutations
from collections import deque

n = int(input())

arr = deque(list(map(int, input().split())))

oper = ['+', '-', '*', '//']
oper_cnt = list(map(int, input().split()))

l_oper = []
for i in range(4):
    if oper_cnt[i]:
        for _ in range(oper_cnt[i]):
            l_oper.append(oper[i])

pro_oper = list(set(permutations(l_oper, len(l_oper))))

answer = []

for p in pro_oper:
    temp = deque(arr)
    modi = ""
    p = deque(p)

    while len(p):
        modi += str(temp.popleft())
        modi += p.popleft()

    modi += str(temp.popleft())

    answer.append(eval(modi))

print(max(answer))
print(min(answer))
