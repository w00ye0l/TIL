import heapq
import sys
input = sys.stdin.readline

n = int(input())

numbers = []

for i in range(n):
    number = int(input())

    if number != 0:
        heapq.heappush(numbers, number)
    else:
        if len(numbers) == 0:
            print(0)
        else:
            print(heapq.heappop(numbers))
