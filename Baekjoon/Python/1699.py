n = int(input())

arr = [i for i in range(n + 1)]
nums = []

for i in range(1, int(n ** (1 / 2)) + 1):
    nums.append(i**2)

for num in nums:
    arr[num] = 1
    for i in range(num, n + 1):
        arr[i] = min(arr[i], arr[i - num] + 1)

print(arr[n])
