def sit(s, arr):
    max_friend, max_empty = -1, -1

    px, py = -1, -1

    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            cur_friend, cur_empty = 0, 0

            if graph[i][j] == 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if not (-1 < nx < N and -1 < ny < N):
                        continue

                    if graph[nx][ny] == 0:
                        cur_empty += 1
                    elif graph[nx][ny] in arr:
                        cur_friend += 1

                if max_friend <= cur_friend:
                    if max_friend == cur_friend:
                        if max_empty <= cur_empty:
                            px, py = i, j
                            max_friend, max_empty = cur_friend, cur_empty
                    else:
                        px, py = i, j
                        max_friend, max_empty = cur_friend, cur_empty

    graph[px][py] = s


N = int(input())

graph = [[0] * N for _ in range(N)]
like = {}

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for _ in range(N**2):
    num, *pick = map(int, input().split())

    sit(num, pick)

    like[num] = pick

answer = 0
for i in range(N):
    for j in range(N):
        temp = 0

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if not (-1 < nx < N and -1 < ny < N):
                continue

            if graph[nx][ny] in like[graph[i][j]]:
                temp += 1

        if temp > 0:
            answer += 10 ** (temp - 1)

print(answer)
