n = int(input())
k = int(input())
coor = list(map(int, input().split()))

coor.sort()

dif = []
for i in range(n - 1):
    dif.append(abs(coor[i] - coor[i + 1]))

dif.sort(reverse=True)

print(sum(dif[k - 1:]))
