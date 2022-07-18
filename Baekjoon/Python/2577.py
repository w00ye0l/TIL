a = int(input())
b = int(input())
c = int(input())

n = a * b * c
arr = [0 for i in range(10)]

while n > 0:
    arr[n % 10] += 1
    n //= 10

for i in range(10):
    print(arr[i])
