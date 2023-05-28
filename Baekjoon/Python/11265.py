import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for _ in range(M):
    A, B, C = map(int, input().split())

    if graph[A - 1][B - 1] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")
