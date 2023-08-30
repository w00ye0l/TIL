import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((a, 0))

    while q:
        nx, cnt = q.popleft()

        if nx == b:
            return cnt

        for i in range(1, N + 1):
            if not visited[i] and arr[nx][i]:
                q.append((i, cnt + 1))
                visited[i] = 1

    return -1


a, b = map(int, input().split())
N, M = map(int, input().split())

visited = [0 for _ in range(N + 1)]
arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())

    arr[s][e], arr[e][s] = 1, 1


print(bfs())
