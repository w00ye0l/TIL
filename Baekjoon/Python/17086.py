import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    Q = deque(shark)

    while Q:
        x, y = Q.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if not (-1 < nx < n and -1 < ny < m):
                continue

            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                Q.append((nx, ny))


n, m = map(int, input().split())

arr = []
shark = []

for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(m):
        if temp[j] == 1:
            shark.append((i, j))

    arr.append(temp)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

bfs()

print(max(map(max, arr)) - 1)
