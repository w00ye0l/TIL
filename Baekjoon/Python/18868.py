m, n = map(int, input().split())

planet = []

for _ in range(m):
    planet.append(list(map(int, input().split())))

cnt = 0
for i in range(m):
    for j in range(i + 1, m):
        temp = 0

        for k in range(n):
            if planet[i][k] > planet[i][k - 1] and planet[j][k] > planet[j][k - 1]:
                temp += 1
            elif planet[i][k] == planet[i][k - 1] and planet[j][k] == planet[j][k - 1]:
                temp += 1
            elif planet[i][k] < planet[i][k - 1] and planet[j][k] < planet[j][k - 1]:
                temp += 1

        if temp == n:
            cnt += 1

print(cnt)
