def solution(start):
    dis[start] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for adj, time in graph[j]:
                if dis[adj] > dis[j] + time:
                    dis[adj] = dis[j] + time

                    if i == n:
                        return True

    return False


tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    dis = [10001 for _ in range(n + 1)]

    for i in range(m):
        s, e, t = map(int, input().split())

        graph[s].append((e, t))
        graph[e].append((s, t))

    for i in range(w):
        s, e, t = map(int, input().split())

        graph[s].append((e, -t))

    negative_cycle = solution(1)
    if negative_cycle:
        print("YES")
    else:
        print("NO")
