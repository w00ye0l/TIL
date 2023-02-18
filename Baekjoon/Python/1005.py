import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    inDegree = [0 for _ in range(n + 1)]
    runningTime = [0 for _ in range(n + 1)]
    queue = deque()

    for _ in range(k):
        x, y = map(int, input().split())

        graph[x].append(y)
        inDegree[y] += 1

    w = int(input())

    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)
            runningTime[i] = time[i - 1]

    while queue:
        cur = queue.popleft()

        for adj in graph[cur]:
            runningTime[adj] = max(runningTime[adj], runningTime[cur] + time[adj - 1])

            inDegree[adj] = max(0, inDegree[adj] - 1)

            if inDegree[adj] == 0:
                queue.append(adj)

    print(runningTime[w])
