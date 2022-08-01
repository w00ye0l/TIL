n = int(input())

milk = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if cnt % 3 == milk[i]:
        cnt += 1

print(cnt)
