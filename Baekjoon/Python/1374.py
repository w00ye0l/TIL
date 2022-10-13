import sys
import heapq

input = sys.stdin.readline

n = int(input())

subject = []
for _ in range(n):
    num, start, end = map(int, input().split())
    subject.append((start, end))

subject.sort()
class_ = []
heapq.heappush(class_, subject[0][1])

for i in range(1, n):
    if subject[i][0] < class_[0]:
        heapq.heappush(class_, subject[i][1])
    else:
        heapq.heappop(class_)
        heapq.heappush(class_, subject[i][1])

print(len(class_))
