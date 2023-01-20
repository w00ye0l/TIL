def cnt(arr):
    cnt = 0
    for i in range(n):
        if arr[i][0] <= 0:
            cnt += 1

    return cnt


def egg_break(idx):
    global result

    if idx == n:
        result = max(result, cnt(eggs))
        return

    if eggs[idx][0] <= 0:
        egg_break(idx + 1)
    else:
        flag = True

        for i in range(len(eggs)):
            if idx != i and eggs[i][0] > 0:
                flag = False
                eggs[i][0] -= eggs[idx][1]
                eggs[idx][0] -= eggs[i][1]

                egg_break(idx + 1)

                eggs[i][0] += eggs[idx][1]
                eggs[idx][0] += eggs[i][1]

        if flag:
            egg_break(n)


n = int(input())

eggs = []

for i in range(n):
    eggs.append(list(map(int, input().split())))


result = 0

egg_break(0)

print(result)
