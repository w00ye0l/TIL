t = int(input())

for _ in range(t):
    n = int(input())

    result = []
    i = 0
    while n > 0:

        if n % 2 == 1:
            result.append(i)

        n //= 2
        i += 1

    print(*result)
