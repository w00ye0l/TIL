def solution():
    cnt = 0

    for i in range(2, n + 1):
        for j in range(1, n + 1):
            if i * j <= n:
                if arr[i * j] == 0:
                    cnt += 1
                    arr[i * j] = 1

                    if cnt == k:
                        print(i * j)
                        return


n, k = map(int, input().split())

arr = [0 for _ in range(n + 1)]

solution()
