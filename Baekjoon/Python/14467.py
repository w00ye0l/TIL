n = int(input())

cow = [[] for _ in range(11)]

for _ in range(n):
    u, v = map(int, input().split())
    cow[u].append(v)

cnt = 0

for i in range(11):
    if len(cow[i]) > 1:
        for j in range(len(cow[i]) - 1):
            if cow[i][j] != cow[i][j + 1]:
                cnt += 1

print(cnt)
