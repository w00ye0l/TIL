n, l = map(int, input().split())
hole = list(map(int, input().split()))

arr = [0] * (max(hole) + 1)

for h in hole:
    arr[h] += 1

i = 1
cnt = 0
while i <= max(hole):
    if arr[i] == 1:
        for j in range(l):
            if i + j > max(hole):
                break

            if arr[i + j] == 1:
                arr[i + j] -= 1

        cnt += 1

    i += 1

print(cnt)
