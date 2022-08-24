n = int(input())

have = list(map(int, input().split()))

dic = {}
for h in have:
    dic[h] = 1

m = int(input())

find = list(map(int, input().split()))

for f in find:
    if f in dic:
        print(1)
    else:
        print(0)
