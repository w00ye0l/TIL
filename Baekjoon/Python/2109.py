from heapq import heappush, heappop

n = int(input())

course = [[] for _ in range(10001)]

for _ in range(n):
    p, d = map(int, input().split())
    course[d].append(p)

heap = []
answer = 0

for i in range(10000, 0, -1):
    for x in course[i]:
        heappush(heap, -x)

    if heap:
        answer += -heappop(heap)

print(answer)
