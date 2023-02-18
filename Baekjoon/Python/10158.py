w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p += t
q += t

p %= 2 * w
q %= 2 * h

if p > w:
    p = 2 * w - p
if q > h:
    q = 2 * h - q

print(p, q)
