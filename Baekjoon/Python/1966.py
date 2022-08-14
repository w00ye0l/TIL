from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    temp = list(map(int, input().split()))

    doc = deque()
    for i in range(n):
        doc.append((i, temp[i]))

    cnt = 0
    while doc:
        max_ = max(doc, key=lambda x: x[1])[1]
        chk = doc.popleft()

        if chk[1] != max_:
            doc.append(chk)
        else:
            cnt += 1

            if chk[0] == m:
                print(cnt)
                break
