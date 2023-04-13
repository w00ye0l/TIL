from collections import deque


def bfs(x, y, sd):
    queue = deque()
    queue.append((x, y, sd, 0))
    visited[x][y][sd] = 1

    while queue:
        # print(queue)
        x, y, d, cnt = queue.popleft()

        if x == ep[0] and y == ep[1] and d == ed:
            return cnt

        # Go k: 1, 2, 3칸 이동하기
        for i in range(1, 4):
            nx = x + dx[d] * i
            ny = y + dy[d] * i

            if not (-1 < nx < m and -1 < ny < n):
                continue

            if visited[nx][ny][d]:
                continue

            if not board[nx][ny]:
                queue.append((nx, ny, d, cnt + 1))
                visited[nx][ny][d] = 1
            else:
                # 중요!! 벽에 막히면 멈춰야 함
                break

        # Turn dir: 회전하기
        for i in range(4):
            if visited[x][y][i]:
                continue

            # 같은 방향이 아닌 경우만 넣어주면 됨
            if d != i:
                visited[x][y][i] = 1

                # 반대되는 방향인 경우만 횟수 2번 추가
                if (
                    (d == 0 and i == 1)
                    or (d == 1 and i == 0)
                    or (d == 2 and i == 3)
                    or (d == 3 and i == 2)
                ):
                    queue.append((x, y, i, cnt + 2))

                # 90도 방향이면 횟수 1번 추가
                else:
                    queue.append((x, y, i, cnt + 1))


m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

*sp, sd = map(int, input().split())
*ep, ed = map(int, input().split())

for i in range(2):
    sp[i] -= 1
    ep[i] -= 1

sd -= 1
ed -= 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(m)]

print(bfs(sp[0], sp[1], sd))
