from collections import deque

n, w, L = map(int, input().split())
arr = deque(list(map(int, input().split())))
Q = deque([0] * w)
weight = 0
answer = 0

while arr:
    weight -= Q.popleft()

    if weight + arr[0] <= L:
        cur = arr.popleft()
        weight += cur
        Q.append(cur)
    else:
        Q.append(0)

    answer += 1

while weight > 0:
    weight -= Q.popleft()
    answer += 1

print(answer)
