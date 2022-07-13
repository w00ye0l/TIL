n = int(input())
arr = list(map(int, input().split()))
d = []

for i in range(24):
    d.append(0)

for i in range(n):
    d[arr[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')
