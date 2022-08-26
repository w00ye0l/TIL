import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    for i in range(m):
        u, v = list(map(int, input().split()))

    print(n - 1)
