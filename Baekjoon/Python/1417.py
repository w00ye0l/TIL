import heapq

n = int(input())

dasom = int(input())

if n == 1:
    print(0)
else:
    vote = []
    for _ in range(n - 1):
        heapq.heappush(vote, (-int(input())))

    cnt = 0
    while True:
        chk = heapq.heappop(vote)

        if -chk >= dasom:
            chk += 1
            dasom += 1

            heapq.heappush(vote, chk)
            cnt += 1
        else:
            break

    print(cnt)
