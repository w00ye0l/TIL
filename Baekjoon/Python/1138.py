from itertools import permutations

n = int(input())

tall = list(map(int, input().split()))

people = [i for i in range(1, n + 1)]

for per in permutations(people, n):
    per = list(per)

    temp = [0 for _ in range(n)]

    for i in range(1, n + 1):
        idx = per.index(i)

        for j in range(0, idx):
            if i < per[j]:
                temp[i - 1] += 1

    if temp == tall:
        print(*per)
