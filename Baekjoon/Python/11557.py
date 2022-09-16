t = int(input())

for _ in range(t):
    n = int(input())

    dic = {}
    for _ in range(n):
        name, cnt = input().split()
        cnt = int(cnt)

        if name not in dic:
            dic[name] = cnt

    dic = sorted(dic.items(), key=lambda x: x[1])

    print(dic[-1][0])
