def solution():
    n, k = map(int, input().split())

    arr = list(map(int, input().split()))

    result = []
    for i in range(n - 1):
        result.append(arr[i + 1] - arr[i])

    return sum(sorted(result, reverse=True)[k - 1 :])


print(solution())
