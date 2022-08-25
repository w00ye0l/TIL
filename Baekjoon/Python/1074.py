import sys
input = sys.stdin.readline

cnt = 0


def zzz(x, y, n):
    global cnt

    if x == r and y == c:
        print(cnt)
        return

    if x <= r < x + n and y <= c < y + n:
        zzz(x, y, n//2)
        zzz(x, y + n//2, n//2)
        zzz(x + n//2, y, n//2)
        zzz(x + n//2, y + n//2, n//2)
    else:
        cnt += n * n


n, r, c = map(int, input().split())

l = 2 ** n

zzz(0, 0, l)
