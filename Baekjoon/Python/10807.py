n = int(input())

arr = list(map(int, input().split()))

dic = {}
for a in arr:
    dic[a] = dic.get(a, 0) + 1

v = int(input())

print(dic.get(v, 0))
