import heapq
import sys
input = sys.stdin.readline

n = int(input())

course = []

for _ in range(n):
    s, t = map(int, input().split())

    course.append((s, t))

course.sort()

heap = []
heapq.heappush(heap, course[0][1])

for i in range(1, n):
    if course[i][0] < heap[0]:
        heapq.heappush(heap, course[i][1])
    else:
        heapq.heapreplace(heap, course[i][1])

print(len(heap))
