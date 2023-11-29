from heapq import heappush, heappop

N = int(input())
M = int(input())
arr = list(map(int, input().split()))
Q = []

for i in range(M):
    temp = []
    flag = False

    while Q:
        cnt, idx, num = heappop(Q)
        if arr[i] == num:
            cnt += 1
            flag = True
        heappush(temp, [cnt, idx, num])

    if not flag:
        if len(temp) >= N:
            heappop(temp)
        heappush(temp, [1, i, arr[i]])

    Q = temp

Q = sorted(list(Q), key=lambda x: x[2])

for v, idx, k in Q:
    print(k, end=" ")
