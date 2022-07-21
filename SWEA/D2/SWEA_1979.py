t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())
    arr = []
    result = 0

    for j in range(n):
        s = list(input().split())
        arr.append(s)

    for a in range(n):
        cnt = 0
        for b in range(n):
            if arr[a][b] == '0' and cnt == k:
                result += 1
            cnt *= int(arr[a][b])

            if arr[a][b] == '1':
                cnt += 1

            if b == n - 1 and cnt == k:
                result += 1

    for b in range(n):
        cnt = 0
        for a in range(n):
            if arr[a][b] == '0' and cnt == k:
                result += 1
            cnt *= int(arr[a][b])

            if arr[a][b] == '1':
                cnt += 1

            if a == n - 1 and cnt == k:
                result += 1

    print(f'#{i} {result}')
