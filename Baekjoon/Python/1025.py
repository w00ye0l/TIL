def checkPerfectSquareNumber(n):
    if (int(n ** (1 / 2))) ** 2 == n:
        return True

    return False


N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

answer = -1

for i in range(N):
    for j in range(M):
        for k in range(-N, N):
            for l in range(-M, M):
                if k == 0 and l == 0:
                    continue

                a, b = i, j
                t = 0

                while -1 < a < N and -1 < b < M:
                    t *= 10
                    t += graph[a][b]

                    if checkPerfectSquareNumber(t):
                        answer = max(answer, t)

                    a += k
                    b += l

                if checkPerfectSquareNumber(t):
                    answer = max(answer, t)

print(answer)
