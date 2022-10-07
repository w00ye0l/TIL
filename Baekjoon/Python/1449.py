n, l = map(int, input().split())
hole = list(map(int, input().split()))

arr = [0] * (max(hole) + 1)

for h in hole:
    arr[h] += 1

cnt = 0
for i in range(1, max(hole) + 1):
    if arr[i] == 1:
        for j in range(l):
            if i + j > max(hole):
                break

            if arr[i + j] == 1:
                arr[i + j] -= 1

        cnt += 1

print(cnt)
