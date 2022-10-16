k = int(input())

build = list(map(int, input().split()))

n = 2**k - 1
result = [[] for _ in range(k)]


def tree(arr, n, k):
    if not arr:
        return
    result[k - 1].append(arr[n // 2])

    tree(arr[: n // 2], n // 2, k - 1)
    tree(arr[n // 2 + 1 :], n // 2, k - 1)


tree(build, n, k)
result.reverse()

for r in result:
    print(*r)
