col, ro = map(int, input().split())
n = int(input())

ro_list = [0, ro]
col_list = [0, col]
ro_gap = []
col_gap = []
area = []

for i in range(n):
    sign, cm = map(int, input().split())
    if sign == 0:
        ro_list.append(cm)
    else:
        col_list.append(cm)

ro_list.sort()
col_list.sort()

for i in range(1, len(ro_list)):
    ro_gap.append(ro_list[i] - ro_list[i - 1])

for i in range(1, len(col_list)):
    col_gap.append(col_list[i] - col_list[i - 1])

for i in range(len(ro_gap)):
    for j in range(len(col_gap)):
        area.append(ro_gap[i] * col_gap[j])

area.sort(reverse=True)

print(area[0])
