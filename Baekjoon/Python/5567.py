# import sys

# input = sys.stdin.readline

# def dfs(x, cnt):
#     if cnt == 1:
#         return

#     for adj in graph[x]:
#         if visited[adj]:
#             continue

#         visited[adj] = 1
#         dfs(adj, cnt + 1)


# n = int(input())
# m = int(input())

# graph = [[] for _ in range(n + 1)]
# visited = [0 for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())

#     graph[a].append(b)
#     graph[b].append(a)

# for adj in graph[1]:
#     visited[adj] = 1
#     dfs(adj, 0)

# print(sum(visited) - visited[1])

import sys

input = sys.stdin.readline


def dfs(x):
    for adj in graph[x]:
        if adj != 1:
            result.add(adj)


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

result = set()

for adj in graph[1]:
    result.add(adj)
    dfs(adj)

print(len(result))
