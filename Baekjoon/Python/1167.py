import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def dfs(n, c):
    for next_node, next_len in graph[n]:
        if dis[next_node] == -1:
            dis[next_node] = c + next_len
            dfs(next_node, c + next_len)


n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n):
    temp = list(map(int, input().split()))

    for i in range(1, len(temp) - 2, 2):
        graph[temp[0]].append((temp[i], temp[i + 1]))

dis = [-1 for _ in range(n + 1)]
dis[1] = 0
dfs(1, 0)

start = dis.index(max(dis))

dis = [-1 for _ in range(n + 1)]
dis[start] = 0
dfs(start, 0)

print(max(dis))
