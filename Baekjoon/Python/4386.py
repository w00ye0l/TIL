import math


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(i, j):
    x = find(i)
    y = find(j)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


n = int(input())

node = []

for i in range(n):
    a, b = map(float, input().split())

    node.append((a, b))

dis = []

for i in range(n):
    for j in range(i + 1, n):
        dis.append(
            (
                i,
                j,
                math.sqrt(
                    (node[i][0] - node[j][0]) ** 2 + (node[i][1] - node[j][1]) ** 2
                ),
            )
        )

dis.sort(key=lambda x: x[2])

parent = [i for i in range(n)]
result = 0

for i in range(len(dis)):
    u, v, cost = dis[i]

    if find(u) != find(v):
        merge(u, v)

        result += cost

print(f"{result:.2f}")
