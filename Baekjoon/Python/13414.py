import sys

input = sys.stdin.readline

k, l = map(int, input().split())

dic = {}
for i in range(l):
    dic[input().rstrip()] = i

dic = sorted(dic.items(), key=lambda x: x[1])[:k]

for d in dic:
    print(d[0])
