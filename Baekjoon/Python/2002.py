n = int(input())

enter = []
for i in range(n):
    enter.append(input())

leave = []
cnt = 0
for i in range(n):
    leave_car = input()
    pre_enter = enter[: enter.index(leave_car)]
    pre_leave = leave

    for pe in pre_enter:
        if not pe in pre_leave:
            cnt += 1
            break

    leave.append(leave_car)

print(cnt)
