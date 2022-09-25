s = list(input())
t = list(input())

while len(s) != len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t = t[::-1]

if s == t:
    print(1)
else:
    print(0)
