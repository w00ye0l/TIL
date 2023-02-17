n = int(input())

arr = list(input())
result = 0

for i in range(n - 1):
    copy_arr = arr[:]
    temp = list(input())
    cnt = 0

    for t in temp:
        if t in copy_arr:
            copy_arr.remove(t)
        else:
            cnt += 1

    if len(copy_arr) <= 1 and cnt <= 1:
        result += 1

print(result)
