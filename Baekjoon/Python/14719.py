H, W = map(int, input().split())
rains = list(map(int, input().split()))

area = [[0 for _ in range(W)] for _ in range(H)]
answer = 0

for i in range(W):
    for j in range(rains[i]):
        area[j][i] = 1

area.reverse()

for i in range(H):
    if area[i].count(1) < 2:
        continue

    flag = False
    cnt = 0

    for j in range(W):
        if area[i][j] == 1:
            if not flag:
                flag = True
            elif flag and cnt:
                answer += cnt
                cnt = 0
        else:
            if flag:
                cnt += 1

print(answer)
