def r_gcd(a, b):
    if b == 0:
        return a
    else:
        return r_gcd(b, a % b)


a, b = map(int, input().split())

print(a * b // r_gcd(a, b))
