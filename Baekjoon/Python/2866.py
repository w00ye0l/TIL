r, c = map(int, input().split())

temp = []
arr = ["" for _ in range(c)]

for _ in range(r):
    temp.append(list(input()))

for i in range(r - 1, -1, -1):
    for j in range(c):
        arr[j] += temp[i][j]

cnt = 0

for i in range(r):
    set_arr = set()

    for j in range(c):
        arr[j] = arr[j][:-1]

        set_arr.add(arr[j])

    if len(set_arr) == len(arr):
        cnt += 1
    else:
        break

print(cnt)
