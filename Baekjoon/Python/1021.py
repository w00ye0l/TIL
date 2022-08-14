from collections import deque

n, m = map(int, input().split())

num = deque([i for i in range(1, n + 1)])
want_num = deque(map(int, input().split()))

cnt = 0
while want_num:
    w = want_num.popleft()
    idx = num.index(w)

    while True:
        p_n = num.popleft()

        if w == p_n:
            break
        else:
            num.appendleft(p_n)

            if idx <= len(num) // 2:
                pl_n = num.popleft()
                num.append(pl_n)
                cnt += 1
            else:
                pr_n = num.pop()
                num.appendleft(pr_n)
                cnt += 1

print(cnt)
