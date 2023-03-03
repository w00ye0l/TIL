import sys

input = sys.stdin.readline

n, k, b = map(int, input().split())

sign = [1 for _ in range(n)]

for _ in range(b):
    sign[int(input()) - 1] = 0


cnt = []
live, die = 0, 0
m = 0

for i in range(n):
    if sign[i] == 1:
        live += 1

    cnt.append(live)

# print(sign)
for i in range(k - 1, n):
    # print(cnt[i], cnt[i - k])
    m = max(m, cnt[i] - cnt[i - k])
# print(cnt)

print(k - m)
