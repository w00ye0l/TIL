import sys
from heapq import heappop, heapify

input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

heap = heapify(arr)

while arr:
    print(heappop(arr))
