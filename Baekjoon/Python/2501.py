N, K = map(int, input().split())
cnt = 0
d = 0

for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1

    if cnt == K:
        d = i
        break

print(d)
