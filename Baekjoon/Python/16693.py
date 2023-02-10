import math

a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())

if a1 / p1 > (r1**2) * math.pi / p2:
    print("Slice of pizza")
else:
    print("Whole pizza")
