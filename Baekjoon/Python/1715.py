import sys
import heapq

input = sys.stdin.readline

n = int(input())

num = []
for _ in range(n):
    heapq.heappush(num, int(input()))

sum_ = 0
if len(num) == 1:
    print(sum_)
else:
    while len(num) > 1:
        first = heapq.heappop(num)
        second = heapq.heappop(num)

        sum_ += first + second
        heapq.heappush(num, first + second)

    print(sum_)
