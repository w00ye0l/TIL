n, m = map(int, input().split())

graph = [[] for _ in range(n)]
answer = 0
visited = [0] * n

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)


def dfs(x, cnt):
    global answer

    if cnt == 5:
        answer = 1
        return

    for adj in graph[x]:
        if visited[adj]:
            continue

        visited[adj] = 1

        dfs(adj, cnt + 1)

        visited[adj] = 0


for i in range(n):
    visited[i] = 1

    dfs(i, 1)

    if answer == 1:
        break

    visited[i] = 0

print(answer)
