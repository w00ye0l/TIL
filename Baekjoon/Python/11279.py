import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    x = int(input())

    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-x, x))
