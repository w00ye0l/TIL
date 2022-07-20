n = int(input())

for i in range(1, n+1):
    cnt = 0
    i = str(i)
    cnt = i.count('3') + i.count('6') + i.count('9')

    if cnt != 0:
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')
