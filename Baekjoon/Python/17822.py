from collections import deque

N, M, T = map(int, input().split())

circles = []

for _ in range(N):
    circles.append((deque(map(int, input().split()))))

for _ in range(T):
    x, d, k = map(int, input().split())

    for i in range(N):
        if (i + 1) % x == 0:
            if d == 0:
                circles[i].rotate(k)
            else:
                circles[i].rotate(-k)

    cnt = 0

    if sum(map(sum, circles)) != 0:
        arr = set()
        for j in range(M):
            num = circles[0][j]

            for i in range(1, N):
                if circles[i][j] == num and circles[i][j] != 0:
                    arr.add((i - 1, j))
                    arr.add((i, j))
                else:
                    num = circles[i][j]

        for i in range(N):
            for j in range(M):
                if circles[i][j] == circles[i][j - 1] and circles[i][j] != 0:
                    arr.add((i, j))
                    arr.add((i, j - 1))

        if arr:
            for x, y in arr:
                circles[x][y] = 0
        else:
            sum_, cnt = 0, 0
            for i in range(N):
                for j in range(M):
                    if circles[i][j] != 0:
                        sum_ += circles[i][j]
                        cnt += 1

            avg = sum_ / cnt

            for i in range(N):
                for j in range(M):
                    if circles[i][j] != 0:
                        if circles[i][j] > avg:
                            circles[i][j] -= 1
                        elif circles[i][j] < avg:
                            circles[i][j] += 1

print(sum(map(sum, circles)))
