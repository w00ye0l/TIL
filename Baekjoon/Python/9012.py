t = int(input())

for i in range(t):
    s = list(input())
    sign = 0

    for j in s:
        if j == '(':
            sign += 1
        elif j == ')':
            sign -= 1

        if sign < 0:
            print('NO')
            break

    if sign > 0:
        print('NO')
    elif sign == 0:
        print('YES')
