import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, K = map(int, input().split())

jewel, C, temp = [], [], []
answer = 0

for _ in range(N):
    heappush(jewel, tuple(map(int, input().split())))

for _ in range(K):
    x = int(input())
    C.append(x)

C.sort()

for c in C:
    while jewel and c >= jewel[0][0]:
        heappush(temp, -jewel[0][1])
        heappop(jewel)

    if temp:
        answer -= heappop(temp)

print(answer)
