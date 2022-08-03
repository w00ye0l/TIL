import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(n)]

sum_ = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_[i][j] = num[i - 1][j - 1] + sum_[i - 1][j] + \
            sum_[i][j - 1] - sum_[i - 1][j - 1]

k = int(input())
for i in range(k):
    i, j, x, y = map(int, input().split())
    print(sum_[x][y] - sum_[x][j - 1] -
          sum_[i - 1][y] + sum_[i - 1][j - 1])
