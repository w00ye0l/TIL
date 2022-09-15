import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    temp = list(map(int, input().split()))

    for t in temp:
        heapq.heappush(heap, t)

        if len(heap) > n:
            heapq.heappop(heap)

print(heapq.heappop(heap))
