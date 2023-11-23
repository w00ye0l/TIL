t = 0

while True:
    t += 1

    n = int(input())
    arr = []

    if n == 0:
        break

    for _ in range(n):
        arr.append([input(), 0])

    for _ in range(2 * n - 1):
        num, alpha = input().split()
        num = int(num) - 1

        arr[num][1] += 1

    for i in range(n):
        if arr[i][1] != 2:
            print(t, arr[i][0])
            break
