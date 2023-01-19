from itertools import combinations

n = int(input())

stat = []

member = [i for i in range(n)]
result = []

for _ in range(n):
    stat.append(list(map(int, input().split())))

for k in range(1, n // 2 + 1):
    for mem in combinations(member, k):
        start, link = 0, 0

        start_mem = set(mem)
        link_mem = list(set(member) - start_mem)
        start_mem = list(start_mem)

        if len(start_mem) != 1:
            for i in range(len(start_mem) - 1):
                for j in range(i + 1, len(start_mem)):
                    start += stat[start_mem[i]][start_mem[j]]
                    start += stat[start_mem[j]][start_mem[i]]

        for i in range(len(link_mem) - 1):
            for j in range(i + 1, len(link_mem)):
                link += stat[link_mem[i]][link_mem[j]]
                link += stat[link_mem[j]][link_mem[i]]

        result.append(abs(start - link))

print(min(result))
