# import heapq
# import sys

# input = sys.stdin.readline

# n = int(input())

# hw = []
# for _ in range(n):
#     hw.append(list(map(int, input().split())))

# hw.sort(key=lambda x: (x[0], -x[1]))

# score = []
# heapq.heappush(score, hw[0][1])
# cnt = 1

# for i in range(1, n):
#     cnt += 1
#     if cnt <= hw[i][0]:
#         heapq.heappush(score, hw[i][1])
#     else:
#         if score[0] < hw[i][1]:
#             heapq.heappop(score)
#             cnt -= 1
#         heapq.heappush(score, hw[i][1])

#     print(score)

# print(sum(score))


import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []
arr = [[] for _ in range(1001)]
m = 0

for _ in range(n):
    d, w = map(int, input().split())
    arr[d].append(w)

    if m < d:
        m = d

# print(arr, m)
answer = 0
for i in range(m, 0, -1):
    for x in arr[i]:
        print(x, arr[i])
        heapq.heappush(heap, -x)
        print(heap)
    if heap:
        answer -= heapq.heappop(heap)
    print(heap)

print(answer)

# import sys

# input = sys.stdin.readline

# n = int(input())

# hw = []
# for _ in range(n):
#     hw.append(list(map(int, input().split())))

# hw.sort()
# score = []
# result = 0
# print(hw)

# for i in range(n, 0, -1):
#     print(hw, hw[-1], i)
#     while hw and hw[-1][0] >= i:
#         score.append(hw.pop()[1])

#     if score:
#         score.sort()
#         result += score.pop()

# print(result)
