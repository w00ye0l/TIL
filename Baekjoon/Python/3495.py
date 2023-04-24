h, w = map(int, input().split())

grid = []

for _ in range(h):
    grid.append(list(input()))

area = 0

for i in range(h):
    flag = False
    for j in range(w):
        if (grid[i][j] == "/" or grid[i][j] == "\\") and not flag:
            flag = True
            area += 0.5
        elif grid[i][j] == "." and flag:
            area += 1
        elif (grid[i][j] == "/" or grid[i][j] == "\\") and flag:
            area += 0.5
            flag = False

print(int(area))
