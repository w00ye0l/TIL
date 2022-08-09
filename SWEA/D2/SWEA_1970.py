t = int(input())

won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tt in range(1, t + 1):
    n = int(input())

    result = []
    for w in won:
        result.append(n // w)
        n %= w

    print(f'#{tt}')
    print(*result)
