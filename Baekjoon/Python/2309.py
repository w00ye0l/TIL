height = []

for i in range(9):
    height.append(int(input()))

check = sum(height) - 100
sign = False

for i in range(8):
    for j in range(i + 1, 9):
        if height[i] + height[j] == check:
            height[i] = 0
            height[j] = 0
            sign = True
            break

    if sign == True:
        break

height.sort()

for i in range(9):
    if height[i] != 0:
        print(height[i])
