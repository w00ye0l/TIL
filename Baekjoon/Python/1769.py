cnt = 0


def three(x):
    global cnt

    if len(x) != 1:
        cnt += 1
        x = list(map(int, str(sum(x))))
        return three(x)
    else:
        return cnt


x = list(map(int, input()))

print(three(x))

if sum(x) % 3 == 0:
    print('YES')
else:
    print('NO')
