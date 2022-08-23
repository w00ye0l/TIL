import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

land = []
for _ in range(n):
    land.append(list(map(int, input().split())))

l_dic = {}

max_ = 0
while max_ <= 256:
    temp = b
    fill = 0
    time = 0
    for i in land:
        for j in i:
            ground = j - max_
            if ground < 0:
                fill += ground
                time += abs(ground)
            else:
                temp += ground
                time += (ground) * 2

    if temp + fill >= 0:
        if max_ not in l_dic:
            l_dic[max_] = time

    max_ += 1

l_dic = sorted(l_dic.items(), key=lambda x: (x[1], -x[0]))

print(*l_dic[0][::-1])
