from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    que = deque()

    tree = list(map(int, input().split()))

    tree.sort()

    que.append(tree.pop())

    cnt = 1
    while tree:
        if cnt % 2 == 1:
            que.append(tree.pop())
        else:
            que.appendleft(tree.pop())

        cnt += 1

    max_ = 0
    for i in range(n):
        if max_ < abs(que[i - 1] - que[i]):
            max_ = abs(que[i - 1] - que[i])

    print(max_)
