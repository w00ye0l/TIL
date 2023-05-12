import sys

input = sys.stdin.readline


def floydWarshall(graph):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            for k in range(1, V + 1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

    return graph


V, E = map(int, input().split())

graph = [[float("inf") for _ in range(V + 1)] for _ in range(V + 1)]
answer = float("inf")

for _ in range(E):
    a, b, c = map(int, input().split())

    graph[a][b] = c

floydWarshall(graph)

for i in range(1, V + 1):
    if answer > graph[i][i]:
        answer = graph[i][i]

print(answer if answer != float("inf") else -1)
