n = int(input())

a = list(map(int, input().split()))
temp = sorted(a)

b = {}
for i in range(n):
    b[i] = temp[i]

for i in range(n):
    for j in range(n):
        if a[i] == b[j]:
            print(j, end=' ')
            b[j] = -1
            break
