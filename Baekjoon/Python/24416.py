n = int(input())

cnt1 = 0
f = [[1, 0], [0, 1]]

for i in range(2, n):
    temp = []
    temp.append(f[i - 1][0] + f[i - 2][0])
    temp.append(f[i - 1][1] + f[i - 2][1])

    f.append(temp)

cnt1 = sum(f[n - 1])

if n == 1 or n == 2:
    cnt2 = 1
else:
    cnt2 = n - 2

print(cnt1, cnt2)
