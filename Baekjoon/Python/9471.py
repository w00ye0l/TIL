import sys

input = sys.stdin.readline

P = int(input())

for _ in range(P):
    N, M = map(int, input().split())

    f, s = 1, 1
    cnt = 3

    while True:
        f, s = s, (f + s) % M
        cnt += 1

        if f == 1 and s == 1:
            print(N, cnt - 3)
            break
