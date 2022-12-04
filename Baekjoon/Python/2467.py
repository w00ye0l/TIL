n = int(input())

arr = list(map(int, input().split()))

arr.sort()

start, end = 0, n - 1
res_start, res_end = arr[start], arr[end]
result = abs(arr[start] + arr[end])

while start < end:
    temp = arr[start] + arr[end]

    if abs(temp) < result:
        result = abs(temp)
        res_start, res_end = arr[start], arr[end]

    if temp < 0:
        start += 1
    else:
        end -= 1

print(res_start, res_end)
