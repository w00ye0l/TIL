def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)

    if cost[x] > cost[y]:
        cost[x] = 0
        parent[x] = y
    else:
        cost[y] = 0
        parent[y] = x


n, m, k = map(int, input().split())

cost = [0] + list(map(int, input().split()))

parent = [i for i in range(n + 1)]

for _ in range(m):
    v, w = map(int, input().split())

    merge(v, w)

sum_ = sum(cost)

if sum_ <= k:
    print(sum_)
else:
    print("Oh no")
