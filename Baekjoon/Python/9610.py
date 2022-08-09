n = int(input())
quadrant = [0] * 5

for _ in range(n):
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        quadrant[1] += 1
    elif x < 0 and y > 0:
        quadrant[2] += 1
    elif x < 0 and y < 0:
        quadrant[3] += 1
    elif x > 0 and y < 0:
        quadrant[4] += 1
    else:
        quadrant[0] += 1

for i in range(1, 5):
    print(f'Q{i}: {quadrant[i]}')
print(f'AXIS: {quadrant[0]}')
