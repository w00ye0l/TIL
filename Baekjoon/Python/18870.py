n = int(input())

num = list(map(int, input().split()))

ch = list(set(num))
ch.sort()

dic = {}
i = 0
for c in ch:
    if c not in dic:
        dic[c] = i
        i += 1

for n in num:
    print(dic[n], end=' ')
