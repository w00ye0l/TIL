import sys
from collections import deque

input = sys.stdin.readline


def move(coin):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    Q = deque()
    Q.append((coin, 0))
    visited = []

    while Q:
        nowCoins, cnt = Q.popleft()
        visited.append(nowCoins)

        if cnt >= 10:
            return -1

        for i in range(4):
            newCoins = []
            c = 0

            for coin in nowCoins:
                newCoin = [coin[0] + dx[i], coin[1] + dy[i]]

                if -1 < newCoin[0] < N and -1 < newCoin[1] < M:
                    if graph[newCoin[0]][newCoin[1]] == "#":
                        newCoin = coin
                else:
                    c += 1

                newCoins.append(newCoin)
            else:
                if c == 1:
                    return cnt + 1
                elif c == 0:
                    if not newCoins in visited:
                        Q.append((newCoins, cnt + 1))

    return -1


N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

coin = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == "o":
            coin.append([i, j])

print(move(coin))
