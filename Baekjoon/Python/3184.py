import sys

sys.setrecursionlimit(10**9)


def dfs(x, y):
    global wolf, sheep, wolf_list, sheep_list

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (-1 < nx < r and -1 < ny < c):
            continue

        if graph[nx][ny] == "#":
            continue

        if visited[nx][ny] == 1:
            continue

        if graph[nx][ny] == "o":
            sheep += 1
            sheep_list.append((nx, ny))
        elif graph[nx][ny] == "v":
            wolf += 1
            wolf_list.append((nx, ny))

        visited[nx][ny] = 1
        dfs(nx, ny)


r, c = map(int, input().split())

graph = []
origin_wolf, origin_sheep = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(c)] for _ in range(r)]

for _ in range(r):
    temp = list(input())

    origin_wolf += temp.count("v")
    origin_sheep += temp.count("o")

    graph.append(temp)

for i in range(r):
    for j in range(c):
        if graph[i][j] == "v":
            wolf, sheep = 1, 0
            wolf_list, sheep_list = [], []
            visited[i][j] = 1
            dfs(i, j)

            if wolf >= sheep:
                origin_sheep -= sheep
                for s in sheep_list:
                    graph[s[0]][s[1]] = "."
            else:
                origin_wolf -= wolf
                for w in wolf_list:
                    graph[w[0]][w[1]] = "."

print(origin_sheep, origin_wolf)
