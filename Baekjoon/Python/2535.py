N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: x[2])

cnt = [0] * 100
answer = []

while arr:
    c, n, p = arr.pop()

    if cnt[c - 1] >= 2:
        continue

    answer.append((c, n))
    cnt[c - 1] += 1

    if sum(cnt) == 3:
        break

for i in range(3):
    print(*answer[i])
