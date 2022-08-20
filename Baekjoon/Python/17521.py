n, w = map(int, input().split())
price = []

for _ in range(n):
    price.append(int(input()))

coin = 0
for i in range(n - 1):
    if price[i] < price[i + 1]:
        if w // price[i] > 0:
            coin = w // price[i]
            w -= price[i] * coin
    elif price[i] > price[i - 1]:
        w += price[i] * coin
        coin = 0

if coin > 0:
    w += coin * price[-1]

print(w)
