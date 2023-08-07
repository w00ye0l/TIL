idx = int(input())
k = int(input())

answer = 0
t = 0

if k % 2:
    if idx == 1:
        t = 1
    elif idx == 2:
        t = 0
    elif idx == 3:
        t = 7
    elif idx == 4:
        t = 6
    elif idx == 5:
        t = 5
else:
    if idx == 1:
        t = 1
    elif idx == 2:
        t = 2
    elif idx == 3:
        t = 3
    elif idx == 4:
        t = 4
    elif idx == 5:
        t = 5

if idx == 1 or idx == 5:
    temp = k * 8 + t
elif idx == 2:
    temp = ((k + 1) // 2) * 8 + t
else:
    temp = (k // 2) * 8 + t

answer = max(0, temp - 1)

print(answer)