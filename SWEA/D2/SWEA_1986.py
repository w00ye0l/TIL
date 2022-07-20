t = int(input())

for a in range(1, t+1):
    n = int(input())
    sign = 1
    result = 0

    for i in range(1, n+1):
        result += i * sign
        sign *= -1

    print(f'#{a} {result}')
