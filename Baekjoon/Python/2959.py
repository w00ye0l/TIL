arr = list(map(int, input().split()))
arr.sort()
print(min(arr[:2]) * min(arr[2:]))
