import math


def cal_dis(a, b):
    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))


crd = []
for _ in range(4):
    crd.append(list(map(int, input().split())))

result = []
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            dis = 0
            if i != j and j != k and k != i:
                dis += cal_dis(crd[0], crd[i])
                dis += cal_dis(crd[i], crd[j])
                dis += cal_dis(crd[j], crd[k])

                result.append(dis)

print(int(min(result)))
