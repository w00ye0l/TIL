def bt(cnt):
    global answer

    if cnt == N:
        p, f, s, v, c = 0, 0, 0, 0, 0
        pick = []

        for i in range(N):
            if visited[i] == 1:
                p += arr[i][0]
                f += arr[i][1]
                s += arr[i][2]
                v += arr[i][3]
                c += arr[i][4]
                pick.append(i + 1)

        if p >= mp and f >= mf and s >= ms and v >= mv:
            answer.append((c, pick))

        return

    visited[cnt] = 1

    bt(cnt + 1)

    visited[cnt] = 0

    bt(cnt + 1)


N = int(input())
mp, mf, ms, mv = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

visited = [0] * N
answer = []

bt(0)

if answer:
    answer.sort()
    print(answer[0][0])
    print(*answer[0][1])
else:
    print(-1)
