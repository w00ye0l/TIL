import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

times = defaultdict(int)

for _ in range(N):
    te, tx = map(int, input().split())

    times[te] += 1
    times[tx] -= 1

m, cnt = 0, 0
st, et = 0, 0
flag = False

for i in sorted(times.keys()):
    cnt += times[i]

    if cnt > m:
        m = cnt
        st = i
        flag = True
    elif cnt < m and cnt - times[i] == m and flag:
        et = i
        flag = False

print(m)
print(st, et)
