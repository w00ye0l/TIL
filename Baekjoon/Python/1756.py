d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))
visited = [0 for _ in range(n)]

for i in range(1, d):
    if oven[i] > oven[i - 1]:
        oven[i] = oven[i - 1]

# print(oven)

idx = 0
for i in range(d - 1, -1, -1):
    print(idx, pizza[idx], i, oven[i])
    if pizza[idx] <= oven[i]:

        visited[idx] = i + 1
        print(visited)
        idx += 1

    if idx == n:
        break

# print(visited)

if idx == n:
    print(visited[idx - 1])
else:
    print(0)
