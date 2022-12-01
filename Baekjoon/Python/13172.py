S = 1000000007


def ans(n, s):
    return s * mul(n, S - 2) % S


def mul(b, t):
    if t == 1:
        return b % S

    if t % 2 == 0:
        tmp = mul(b, t // 2)
        return (tmp * tmp) % S
    else:
        return b * mul(b, t - 1) % S


SUM = 0

m = int(input())

for _ in range(m):
    n, s = map(int, input().split())
    SUM += ans(n, s)
    SUM %= S

print(SUM)
