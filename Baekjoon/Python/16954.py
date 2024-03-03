arr = [list(input()) for _ in range(8)]

chars = [(7, 0)]
newChars = []
dr = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
answer = 1

for _ in range(8):
    while chars:
        x, y = chars.pop()
        if arr[x][y] == "#":
            continue
        else:
            for dx, dy in dr:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < 8 and 0 <= ny < 8):
                    continue

                if arr[nx][ny] == "#":
                    continue

                if (nx, ny) not in newChars:
                    newChars.append((nx, ny))

    arr.pop()
    arr.insert(0, [".", ".", ".", ".", ".", ".", ".", "."])

    if not newChars:
        answer = 0

    chars = newChars
    newChars = []

if answer:
    print(1)
else:
    print(0)
