# 유니온 파인드

import sys

input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


n, m = map(int, input().split())

parent = [i for i in range(n)]
answer = 0

for i in range(m):
    u, v = map(int, input().split())

    pu, pv = find(u), find(v)

    if pu == pv and not answer:
        answer = i + 1
        break

    merge(u, v)

print(answer)
