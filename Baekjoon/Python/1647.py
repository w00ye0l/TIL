import sys

input = sys.stdin.readline


def findParent(x):
    if x != parent[x]:
        parent[x] = findParent(parent[x])

    return parent[x]


def merge(x, y):
    x = findParent(x)
    y = findParent(y)

    if x == y:
        return

    parent[y] = x


n, m = map(int, input().split())

edges = []
parent = [i for i in range(n + 1)]
answer = 0

for _ in range(m):
    a, b, c = map(int, input().split())

    edges.append((c, a, b))

edges.sort()

for c, u, v in edges:
    if findParent(u) != findParent(v):
        merge(u, v)
        answer += c
        max_cost = c

answer -= max_cost

print(answer)
