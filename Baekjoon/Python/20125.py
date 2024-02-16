def findHead():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "*":
                return (i + 1, j)


N = int(input())
arr = [input() for _ in range(N)]

h = findHead()
lh, rh, b, ll, rl = 0, 0, 0, 0, 0
ls = (0, 0)

for i in range(h[1] - 1, -1, -1):
    if arr[h[0]][i] == "*":
        lh += 1

for i in range(h[1] + 1, N):
    if arr[h[0]][i] == "*":
        rh += 1

for i in range(h[0] + 1, N):
    if arr[i][h[1]] == "*":
        b += 1
        ls = (i + 1, h[1])

for i in range(h[0] + 1, N):
    if arr[i][h[1] - 1] == "*":
        ll += 1
    if arr[i][h[1] + 1] == "*":
        rl += 1

print(h[0] + 1, h[1] + 1)
print(lh, rh, b, ll, rl)
