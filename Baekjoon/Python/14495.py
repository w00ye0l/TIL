n = int(input())

arr = [1, 1, 1]

for i in range(3, n):
    arr.append(arr[i - 1] + arr[i - 3])

print(arr[n - 1])
