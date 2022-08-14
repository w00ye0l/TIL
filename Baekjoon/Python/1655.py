import heapq
import sys
input = sys.stdin.readline

n = int(input())

s_heap = []
b_heap = []
num = int(input())
mid = num
print(f'mid = {mid}')

for i in range(1, n):
    num = int(input())

    if mid < num:
        heapq.heappush(b_heap, num)
        if len(s_heap) < len(b_heap):
            mid = num
            print(mid)
