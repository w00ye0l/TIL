N, M = map(int, input().split())

graph = [[0] * 100 for _ in range(100)]
answer = 0

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(min(x1, x2) - 1, max(x1, x2)):
        for j in range(min(y1, y2) - 1, max(y1, y2)):
            graph[i][j] += 1

for i in range(100):
    for j in range(100):
        if graph[i][j] > M:
            answer += 1

print(answer)
