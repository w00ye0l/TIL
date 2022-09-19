n = int(input())

for a in range(1, n + 1):
    for i in range(n - a):
        print(' ', end='')
    for j in range(a):
        print('*', end='')
    print()

for a in range(n - 1, 0, -1):
    for i in range(n - a):
        print(' ', end='')
    for j in range(a):
        print('*', end='')
    print()
