t = int(input())

arr = [0] * 1000000
arr[0] = 1
arr[1] = 2
arr[2] = 4

num = []
for _ in range(t):
    num.append(int(input()))

for i in range(3, max(num)):
    arr[i] = (arr[i - 1] + arr[i - 2] + arr[i - 3]) % 1000000009

for n in num:
    print(arr[n - 1])
