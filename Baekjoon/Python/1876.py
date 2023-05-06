import math

n = int(input())

for _ in range(n):
    t, x = input().split()
    t, x = float(t), int(x)
    cal_x = math.pi * (x / 180)

    temp_sin = 0.16 / math.sin(cal_x)
    start = t - temp_sin
    end = t + temp_sin
    move = (1.05 - 0.2) / math.tan(cal_x)
    answer = False

    dis = 0

    while dis < end:
        if start < dis < end:
            answer = True
            break

        dis += move

    if answer:
        print("yes")
    else:
        print("no")
