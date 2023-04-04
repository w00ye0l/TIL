INF = float("inf")


def power(a, b):
    if a == 0:
        return 2
    elif a == b:
        return 1
    elif abs(a - b) % 2 == 1:
        return 3
    else:
        return 4


move = list(map(int, input().split()))

n = len(move)
if n == 1:
    print(0)
else:
    dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(n)]

    # 초기값 (0, 0)일 때, 0
    dp[-1][0][0] = 0

    for i in range(n - 1):
        # 현재 이동해야 할 곳
        now = move[i]

        # j는 움직이지 않는 발, k는 움직이는 발
        for j in range(5):
            for k in range(5):
                # k에서 현재 이동해야 할 곳으로 옮기는 힘
                add = power(k, now)

                # dp[i][왼발][오른발]

                # 왼발을 옮겼을 경우, j를 오른발에 고정
                dp[i][now][j] = min(dp[i][now][j], dp[i - 1][k][j] + add)

                # 오른발을 옮겼을 경우, j를 왼발에 고정
                dp[i][j][now] = min(dp[i][j][now], dp[i - 1][j][k] + add)

    # 0을 제외하고 마지막이기 때문에 [n - 2]
    print(min(map(min, dp[n - 2])))
