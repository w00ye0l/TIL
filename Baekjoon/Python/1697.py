from collections import deque

n, k = map(int, input().split())

visited = [0] * (100001)

queue = deque()
queue.append(n)

while queue:
    cur = queue.popleft()

    if cur == k:
        break

    dis = [cur - 1, cur + 1, 2 * cur]

    for d in dis:
        if -1 < d < 100001:
            if visited[d] == 0:
                visited[d] = visited[cur] + 1
                queue.append(d)

print(visited[k])
