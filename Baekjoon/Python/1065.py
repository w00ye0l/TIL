n = input()
cnt = 0

if len(n) == 1 or len(n) == 2:
    cnt = n
else:
    for i in range(100, int(n) + 1):
        arr = list(map(int, list(str(i))))
        if arr[2]-arr[1] == arr[1]-arr[0]:
            cnt += 1
    cnt += 99

print(cnt)
