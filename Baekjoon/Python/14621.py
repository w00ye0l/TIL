import sys

input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(u, v):
    x = find(u)
    y = find(v)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


n, m = map(int, input().split())

gender = list(map(str, input().split()))

edge = []
for _ in range(m):
    edge.append(tuple(map(int, input().split())))

edge.sort(key=lambda x: x[2])

parent = [i for i in range(n + 1)]
visited = [0 for _ in range(n)]
result = 0

for u, v, d in edge:
    if gender[u - 1] != gender[v - 1]:
        if find(u) != find(v):
            merge(u, v)

            visited[u - 1], visited[v - 1] = 1, 1
            result += d

if 0 in visited:
    print(-1)
else:
    print(result)
