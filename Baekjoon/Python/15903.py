import heapq

n, m = map(int, input().split())
card = list(map(int, input().split()))

score = []
for c in card:
    heapq.heappush(score, c)

while m > 0:
    m -= 1

    x = heapq.heappop(score)
    y = heapq.heappop(score)

    heapq.heappush(score, (x + y))
    heapq.heappush(score, (x + y))

print(sum(score))
