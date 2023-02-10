arr = list(map(int, input().split()))

arr.sort()

print(arr[0] + arr[1] + min(arr[2], (arr[0] + arr[1] - 1)))
