N, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer_cnt = 0
answer = [0, 0]
sx, ex, sy, ey = 100, -100, 100, -100

for i in range(N):
    sx = min(sx, arr[i][0])
    ex = max(ex, arr[i][0])
    sy = min(sy, arr[i][1])
    ey = max(ey, arr[i][1])

for i in range(sx, ex + 1):
    for j in range(sy, ey + 1):
        cnt = 0
        for k in range(N):
            d = ((i - arr[k][0]) ** 2 + (j - arr[k][1]) ** 2) ** (1 / 2)

            if d <= R:
                cnt += 1

        if answer_cnt < cnt:
            answer_cnt = cnt
            answer = [i, j]

print(*answer)
