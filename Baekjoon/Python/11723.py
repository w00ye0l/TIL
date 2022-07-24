import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
s = set()

for i in range(n):
    arr = input().split()

    if len(arr) == 1:
        if arr[0] == 'all':
            s = set([i for i in range(1, 21)])
        elif arr[0] == 'empty':
            s = set()
    else:
        order, number = arr[0], arr[1]
        number = int(number)

        if order == 'add':
            s.add(number)
        elif order == 'remove':
            s.discard(number)
        elif order == 'check':
            if number in s:
                print('1')
            else:
                print('0')
        elif order == 'toggle':
            if number in s:
                s.discard(number)
            else:
                s.add(number)
