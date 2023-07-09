X, Y, W, S = map(int, input().split())

first = (X + Y) * W
if (X + Y) % 2 == 0:
    second = max(X, Y) * S
else:
    second = (max(X, Y) - 1) * S + W
third = min(X, Y) * S + abs(X - Y) * W

print(min(first, second, third))
