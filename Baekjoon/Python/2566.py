arr = []

for _ in range(9):
    arr.append(list(map(int, input().split())))

max_, x, y = 0, 0, 0
for i in range(9):
    for j in range(9):
        if max_ < arr[i][j]:
            max_ = arr[i][j]
            x, y = i, j

print(max_)
print(x + 1, y + 1)
