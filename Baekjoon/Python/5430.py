from collections import deque

t = int(input())

for _ in range(t):
    fun = input()
    n = int(input())
    num = deque(input()[1:-1].split(','))
    result = True

    cnt = 0
    for f in fun:
        if f == 'R':
            cnt += 1
        elif f == 'D':
            if not num or n == 0:
                result = False
                break
            else:
                if cnt % 2 == 0:
                    num.popleft()
                else:
                    num.pop()

    if result:
        print('[', end='')

        if cnt % 2 == 0:
            print(*num, sep=',', end='')
        else:
            num.reverse()
            print(*num, sep=',', end='')

        print(']')
    else:
        print('error')
