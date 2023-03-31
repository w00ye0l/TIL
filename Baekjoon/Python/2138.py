n = int(input())

light = list(map(int, input()))
result = list(map(int, input()))


def solve():
    # 첫 번째 전구를 킨 경우
    temp = light[:]
    cnt1 = 1

    temp[0] = not temp[0]
    temp[1] = not temp[1]

    for i in range(1, n):
        if temp[i - 1] != result[i - 1]:
            cnt1 += 1

            temp[i - 1] = not temp[i - 1]
            temp[i] = not temp[i]

            if i != n - 1:
                temp[i + 1] = not temp[i + 1]

    if temp != result:
        cnt1 = -1

    # 첫 번째 전구를 키지 않은 경우
    temp = light[:]
    cnt2 = 0

    for i in range(1, n):
        if temp[i - 1] != result[i - 1]:
            cnt2 += 1

            temp[i - 1] = not temp[i - 1]
            temp[i] = not temp[i]

            if i != n - 1:
                temp[i + 1] = not temp[i + 1]

    if temp != result:
        cnt2 = -1

    if cnt1 != -1 and cnt2 != -1:
        print(min(cnt1, cnt2))
    elif cnt1 == -1:
        print(cnt2)
    elif cnt2 == -1:
        print(cnt1)
    else:
        print(-1)


solve()
