n = int(input())

ball = [0, 1, 2, 3]

for _ in range(n):
    x, y = map(int, input().split())

    x_idx = ball.index(x)
    y_idx = ball.index(y)

    ball[x_idx], ball[y_idx] = ball[y_idx], ball[x_idx]

print(ball[1])
