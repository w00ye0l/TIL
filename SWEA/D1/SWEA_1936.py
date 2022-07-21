a, b = map(int, input().split())
win = a if a > b else b

if a == 1 and b == 3:
    win = a
elif a == 3 and b == 1:
    win = b

if win == a:
    print('A')
else:
    print('B')
