from collections import deque

n = int(input())
arr = deque([str(i) for i in range(1, n + 1)])
result = []

while len(arr) != 1:
    result.append(arr.popleft())
    arr.append(arr.popleft())

result.append(arr.pop())

print(*result)
