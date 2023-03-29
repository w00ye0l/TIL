r1, c1, r2, c2 = map(int, input().split())

board = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

# 반복할 횟수
step = (c2 - c1 + 1) * (r2 - r1 + 1)

# 초기 위치
x = y = 0
# 1부터 시작
num = 1
# 이동 횟수
cnt = 0
# 방향
d = 0
# 현재 방향으로 이동해야 할 횟수
dcnt = 1

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

while step:
    if r1 <= x <= r2 and c1 <= y <= c2:
        step -= 1
        board[x - r1][y - c1] = num
        # 조건에 맞는 수가 최종적으로 가장 큰 수가 됨
        max_ = num

    # 수를 증가시키고 이동 횟수도 증가시킴
    num += 1
    cnt += 1

    # 위치 이동
    y += dy[d]
    x += dx[d]

    # 이동 횟수가 현재 방향으로 이동해야 할 횟수라면
    if cnt == dcnt:
        # 이동 횟수를 초기화
        cnt = 0
        # 방향 전환
        d = (d + 1) % 4

        # 만약 방향이 왼쪽으로 가거나 오른쪽으로 갈 때
        if d == 0 or d == 2:
            # 이동해야 할 횟수를 증가시켜야 함
            dcnt += 1

# 가장 큰 수의 길이
max_len = len(str(max_))

for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        # rjust는 오른쪽 정렬, rjust(총 길이, 남은 칸에 채울 문자)로 사용
        print(str(board[i][j]).rjust(max_len, " "), end=" ")
    print()
