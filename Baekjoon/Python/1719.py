def floydWarShall():
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                dis[i][j] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
                    route[i][j] = route[i][k]


INF = float("inf")

n, m = map(int, input().split())

dis = [[INF] * (n + 1) for _ in range(n + 1)]
route = [["-"] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v, c = map(int, input().split())
    dis[u][v] = c
    dis[v][u] = c
    route[u][v] = str(v)
    route[v][u] = str(u)

floydWarShall()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print("-", end=" ")
        else:
            print(route[i][j], end=" ")
    print()
