n, m = map(int, input().split())

basket = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())

    for idx in range(i - 1, j):
        basket[idx] = k

print(*basket)
