import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def calCost(x, y):
    cost = []

    for i in range(3):
        cost.append(abs(x[i] - y[i]))

    return min(cost)


def mst():
    heap = []
    heap.append((0, 0))
    visited = [0] * N
    answer = 0
    cnt = 0

    while heap:
        if cnt == N:
            break

        cost, node = heappop(heap)

        if visited[node]:
            continue

        visited[node] = 1
        answer += cost
        cnt += 1

        for adj in dis[node]:
            heappush(heap, adj)

    return answer


N = int(input())

planet = []
for i in range(N):
    planet.append(list(map(int, input().split())) + [i])

dis = [[] for _ in range(N)]

for i in range(3):
    planet.sort(key=lambda x: x[i])
    for j in range(1, N):
        n1 = planet[j - 1]
        n2 = planet[j]

        dis[n1[3]].append((calCost(n1, n2), n2[3]))
        dis[n2[3]].append((calCost(n1, n2), n1[3]))

print(mst())
