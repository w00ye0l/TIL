import math

r, c, n = map(int, input().split())

print(math.ceil(r / n) * math.ceil(c / n))
