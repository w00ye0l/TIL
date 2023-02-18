x, y, d, t = map(int, input().split())

dis = (x**2 + y**2) ** 0.5

result = [dis, t + abs(d - dis)]

for i in range(2, 2001):
    if dis > i * d:
        result.append(i * t + dis - i * d)
    else:
        result.append(i * t)

print(min(result))
