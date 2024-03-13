from math import gcd

A, B = map(int, input().split())
C, D = map(int, input().split())

numerator, denominator = (A * D) + (C * B), B * D
divide = gcd(numerator, denominator)

if divide != 1:
    numerator //= divide
    denominator //= divide

print(numerator, denominator)
