from itertools import combinations

n, m = map(int, input().split())

city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))

chi_list = list(combinations(chicken, m))

result = []
for c_l in chi_list:
    sum_ = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                temp = []
                for c in c_l:
                    temp.append(abs(c[0] - i) + abs(c[1] - j))
                sum_ += min(temp)

    result.append(sum_)

print(min(result))
