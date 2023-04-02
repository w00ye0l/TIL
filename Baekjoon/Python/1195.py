part1 = list(map(int, input()))
part2 = list(map(int, input()))

n = len(part1)
m = len(part2)
cnt = 0

if n > m:
    part1, part2 = part2, part1
    n, m = len(part1), len(part2)

for t in range(n):
    for i in range(t + 1):
        if part1[-t + i - 1] + part2[i] == 4:
            break
    else:
        cnt = max(cnt, t + 1)

    for i in range(t + 1):
        if part1[i] + part2[-t + i - 1] == 4:
            break
    else:
        cnt = max(cnt, t + 1)

for t in range(m - n + 1):
    for i in range(n):
        if part1[i] + part2[i + t] == 4:
            break
    else:
        cnt = max(cnt, n)
        break

print(n + m - cnt)
