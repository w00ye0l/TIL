import heapq
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

beer = [list(map(int, input().split())) for _ in range(k)]
beer = sorted(beer, key=lambda x: (x[1], x[0]))

cnt, sum_ = 0, 0
result = []
for b in beer:
    sum_ += b[0]
    heapq.heappush(result, b[0])
    cnt += 1

    if cnt == n:
        if sum_ >= m:
            answer = b[1]
            break
        else:
            cnt -= 1
            sum_ -= heapq.heappop(result)

else:
    print(-1)
    exit()
print(answer)
