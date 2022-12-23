from collections import deque

n = int(input())

apple = []
for _ in range(int(input())):
    apple.append(list(map(int, input().split())))

turns = []
for _ in range(int(input())):
    x, c = input().split()
    turns.append([int(x), c])

snake = deque()
snake.append([1, 1])

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
m = 0
time = 0

while True:
    time += 1

    new = [snake[-1][0] + move[m][0], snake[-1][1] + move[m][1]]

    if not (0 < new[0] <= n and 0 < new[1] <= n):
        break

    if new in snake:
        break

    snake.append(new)

    if new not in apple:
        snake.popleft()
    else:
        apple.pop(apple.index(new))

    for turn in turns:
        if time == turn[0]:
            if turn[1] == "D":
                m += 1
            elif turn[1] == "L":
                m -= 1

            if m == 4:
                m = 0
            elif m < 0:
                m = 3

print(time)
