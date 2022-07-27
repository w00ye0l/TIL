t = int(input())

for i in range(1, t + 1):
    n = int(input())
    arr = []

    for j in range(n):
        s = []
        for k in range(j+1):
            s.append(1)
        arr.append(s)

    for j in range(2, n):
        for k in range(1, j):
            arr[j][k] = arr[j-1][k-1] + arr[j-1][k]

    print(f'#{i}')
    for j in range(n):
        for k in arr[j]:
            print(k, end=' ')
        print()
