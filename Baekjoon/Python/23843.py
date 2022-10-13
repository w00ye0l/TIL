import heapq

n, m = map(int, input().split())
con = [0] * m

charge = list(map(int, input().split()))
charge.sort()
heapq.heapify(con)

for i in range(n):
    temp = heapq.heappop(con)

    temp += charge.pop()
    heapq.heappush(con, temp)

print(max(con))
