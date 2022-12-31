import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

korean = math.ceil(a / c)
math_ = math.ceil(b / d)

print(l - max(korean, math_))
