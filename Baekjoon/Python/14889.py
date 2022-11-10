import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

member = set([i for i in range(n)])

s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

members = list(set(combinations(member, n // 2)))

result = []
for mem1 in members[: len(members)]:
    mem2 = list(member.difference(mem1))

    sum1, sum2 = 0, 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            sum1 += s[mem1[i]][mem1[j]] + s[mem1[j]][mem1[i]]
            sum2 += s[mem2[i]][mem2[j]] + s[mem2[j]][mem2[i]]

    result.append(abs(sum1 - sum2))

print(min(result))
