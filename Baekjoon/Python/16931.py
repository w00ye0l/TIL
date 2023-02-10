n, m = map(int, input().split())

boxes = []
result = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    boxes.append(list(map(int, input().split())))


for i in range(n):
    for j in range(m):
        result[i][j] += boxes[i][j] * 6 - (boxes[i][j] - 1) * 2

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if not (-1 < nx < n and -1 < ny < m):
                continue

            result[i][j] -= min(boxes[i][j], boxes[nx][ny])

print(sum(map(sum, result)))
