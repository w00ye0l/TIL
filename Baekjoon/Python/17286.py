import math

yumi = []
check = [0 for _ in range(4)]

for i in range(4):
    yumi.append(list(map(int, input().split())))

i = 0
cnt = 0
result = 0
while cnt != 4:
    min_ = math.inf
    min_idx = 0
    check[i] = 1

    for j in range(4):
        if check[j] == 0:
            dis = math.sqrt((yumi[i][0] - yumi[j][0]) **
                            2 + (yumi[i][1] - yumi[j][1]) ** 2)
            if dis < min_:
                min_ = dis
                min_idx = j

    i = min_idx
    if min_ != math.inf:
        result += min_

    cnt += 1

print(math.floor(result))
