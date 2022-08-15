import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

cnt = 1


def dfs(visited, graph, start):
    global cnt
    visited[start] = cnt

    for adj in graph[start]:
        if not visited[adj]:
            cnt += 1
            dfs(visited, graph, adj)


n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

dfs(visited, graph, r)

for i in range(1, n + 1):
    print(visited[i])
