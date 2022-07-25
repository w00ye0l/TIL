n = int(input())

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print('* ', end='')
        else:
            print(' *', end='')
    print()
