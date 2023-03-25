n, m = map(int, input().split())

basket = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    basket[i - 1 : j] = reversed(basket[i - 1 : j])

print(*basket)
