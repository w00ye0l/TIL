n, m = map(int, input().split())

basket = [i for i in range(1, n + 1)]

for _ in range(m):
    begin, end, mid = map(int, input().split())

    basket[begin - 1 : end] = basket[mid - 1 : end] + basket[begin - 1 : mid - 1]

print(*basket)
