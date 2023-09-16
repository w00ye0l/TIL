N = int(input())

arr = list(map(int, input().split()))

arr.sort()
M = 0

if N % 2:
    for i in range(N // 2):
        M = max(M, arr[i] + arr[-i - 2])

    M = max(M, arr[-1])
else:
    for i in range(N // 2):
        M = max(M, arr[i] + arr[-i - 1])

print(M)
