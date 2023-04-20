def getFibonacci():
    arr = [0, 1]
    n = 2

    while True:
        temp = arr[n - 1] + arr[n - 2]
        if temp <= 1000000000:
            arr.append(temp)
            n += 1
        else:
            break

    return arr


arr = getFibonacci()

for _ in range(int(input())):
    n = int(input())
    result = []

    for i in range(len(arr) - 1, 0, -1):
        if n >= arr[i]:
            n -= arr[i]
            result.append(arr[i])

    print(*reversed(result))
