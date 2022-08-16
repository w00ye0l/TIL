import sys
sys.setrecursionlimit(10 ** 6)


def dfs(n):
    for i in graph[n]:
        if parent[i] == 0:
            parent[i] = n
            dfs(i)


n = int(input())

graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])
