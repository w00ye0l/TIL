from itertools import accumulate
from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

pA = [0] + list(accumulate(A))
pB = [0] + list(accumulate(B))

a_dic = defaultdict(int)
b_dic = defaultdict(int)

for i in range(1, n + 1):
    for j in range(i):
        a_dic[pA[i] - pA[j]] += 1

for i in range(1, m + 1):
    for j in range(i):
        b_dic[pB[i] - pB[j]] += 1

answer = 0

for i in a_dic.keys():
    if T - i in b_dic.keys():
        answer += a_dic[i] * b_dic[T - i]

print(answer)
