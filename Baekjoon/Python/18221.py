N = int(input())

arr = []

for i in range(N):
    temp = list(map(int, input().split()))

    for j in range(N):
        if temp[j] == 2:
            sg = (i, j)
        if temp[j] == 5:
            pro = (i, j)

    arr.append(temp)

dis = ((sg[0] - pro[0]) ** 2 + (sg[1] - pro[1]) ** 2) ** 0.5
cnt = 0
answer = 0

if dis >= 5:
    for i in range(min(sg[0], pro[0]), max(sg[0], pro[0]) + 1):
        for j in range(min(sg[1], pro[1]), max(sg[1], pro[1]) + 1):
            if arr[i][j] == 1:
                cnt += 1

    if cnt >= 3:
        answer = 1

print(answer)
