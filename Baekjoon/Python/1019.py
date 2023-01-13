n = int(input())

num = [0 for _ in range(10)]


def calc(x, num, point):
    while x > 0:
        num[x % 10] += point
        x //= 10


start, point = 1, 1

while True:
    while n % 10 != 9 and start <= n:
        calc(n, num, point)
        n -= 1

    if n < start:
        break

    while start % 10 != 0 and start <= n:
        calc(start, num, point)
        start += 1

    start //= 10
    n //= 10

    for i in range(10):
        num[i] += n * point

    point *= 10

print(*num)
