N = int(input())
arr = list(map(int, input().split()))
T = int(input())

for _ in range(T):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(num - 1, N, num):
            arr[i] = 1 if arr[i] == 0 else 0
    elif sex == 2:
        start, end = num - 1, num - 1
        arr[start] = 1 if arr[start] == 0 else 0

        while True:
            start -= 1
            end += 1

            if start < 0 or end >= N:
                break

            if arr[start] == arr[end]:
                arr[start] = 1 if arr[start] == 0 else 0
                arr[end] = 1 if arr[end] == 0 else 0
            else:
                break

i, cnt = 0, 0

while i < N:
    print(arr[i], end=" ")
    cnt += 1
    i += 1

    if cnt == 20:
        print()
        cnt = 0
