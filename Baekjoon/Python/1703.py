while True:
    arr = list(map(int, input().split()))
    leaf = 1

    if arr[0] == 0:
        break

    for i in range(1, len(arr) - 1, 2):
        leaf *= arr[i]
        leaf -= arr[i + 1]

    print(leaf)
