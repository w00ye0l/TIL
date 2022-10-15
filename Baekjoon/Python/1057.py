n, kim, im = map(int, input().split())

arr = [0 for _ in range(n)]
arr[kim - 1] = 1
arr[im - 1] = 1

cnt = 0
flag = False
while len(arr) != 1:
    temp = []
    cnt += 1
    if len(arr) % 2 == 1:
        m = len(arr) - 1
    else:
        m = len(arr)

    for i in range(0, m, 2):
        win = 0

        if arr[i] * arr[i + 1] == 1:
            flag = True
            break

        if arr[i] == 1 or arr[i + 1] == 1:
            win = 1
        temp.append(win)

    if len(arr) % 2 == 1:
        temp.append(arr[-1])

    if flag:
        break

    arr = temp

if flag:
    print(cnt)
else:
    print(-1)
