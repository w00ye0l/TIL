def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n, m = map(int, input().split(':'))

gcd_ = gcd(n, m)

print(f'{n // gcd_}:{m // gcd_}')
