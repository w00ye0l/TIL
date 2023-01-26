import sys

input = sys.stdin.readline

n = int(input())

house = []

for _ in range(n):
    house.append(list(map(int, input().split())))

cnt = 0


def dfs(x, y, direction):
    global cnt

    if (x, y) == (n - 1, n - 1):
        cnt += 1
        return

    if direction == 0 or direction == 2:
        nx, ny = x, y + 1
        if ny < n and house[nx][ny] == 0:
            dfs(nx, ny, 0)

    if direction == 1 or direction == 2:
        nx, ny = x + 1, y
        if nx < n and house[nx][ny] == 0:
            dfs(nx, ny, 1)

    if x + 1 < n and y + 1 < n:
        if house[x][y + 1] == 0 and house[x + 1][y] == 0 and house[x + 1][y + 1] == 0:
            dfs(x + 1, y + 1, 2)


dfs(0, 1, 0)

print(cnt)
