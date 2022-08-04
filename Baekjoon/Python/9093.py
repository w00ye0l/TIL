n = int(input())

for _ in range(n):
    s = list(input().split())
    re_s = []

    for i in s:
        re_s.append(i[::-1])

    print(' '.join(re_s))
