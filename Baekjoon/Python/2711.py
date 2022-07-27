t = int(input())

for i in range(t):
    number, s = input().split()

    number = int(number)
    s = list(s)

    s.pop(number - 1)

    print(''.join(s))
