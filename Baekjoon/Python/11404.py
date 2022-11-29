import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())

costs = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

m = int(input())

for i in range(m):
    a, b, c = map(int, input().split())
    costs[a][b] = min(costs[a][b], c)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if j == k:
                costs[j][k] = 0
            else:
                costs[j][k] = min(costs[j][k], costs[j][i] + costs[i][k])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if costs[i][j] == INF:
            print(0, end=" ")
        else:
            print(costs[i][j], end=" ")
    print()
