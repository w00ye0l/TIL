import sys

sys.stdin = open('SWEA_1204.txt')

t = int(input())

for i in range(t):
    dic = {}

    c = int(input())
    arr = list(map(int, input().split()))

    for j in arr:
        if not j in dic:
            dic[j] = 1
        else:
            dic[j] += 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    result = dic[0][0]

    print(f'#{c} {result}')
