import sys
from heapq import heappush, heappop

input = sys.stdin.readline

while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    node = [[] for _ in range(m)]
    visited = [0] * m
    before = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        before += z

        node[x].append((z, y))
        node[y].append((z, x))

    heap = [[0, 0]]
    answer = 0
    cnt = 0

    while heap:
        if cnt == m:
            break

        w, s = heappop(heap)

        if not visited[s]:
            visited[s] = 1
            answer += w
            cnt += 1

            for i in node[s]:
                heappush(heap, i)

    print(before - answer)
