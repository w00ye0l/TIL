import math

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))

    n = arr[0]
    arr = arr[1:]
    result = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            result += math.gcd(arr[i], arr[j])

    print(result)
