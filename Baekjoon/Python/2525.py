a, b = map(int, input().split())
c = int(input())
n, m = a, b + c

if m >= 60:
    n += m // 60
    m %= 60
    if n >= 24:
        n -= 24

print(n, m)
