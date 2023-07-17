import sys

input = sys.stdin.readline

N = int(input())

p = [tuple(map(int, input().split())) for _ in range(N)]

p.sort(key=lambda x: (x[1], x[0]))

answer = 0

for i in range(N):
    if i == 0:
        if p[i][1] == p[i + 1][1]:
            answer += p[i + 1][0] - p[i][0]
    elif i == N - 1:
        if p[i - 1][1] == p[i][1]:
            answer += p[i][0] - p[i - 1][0]
    else:
        if p[i][1] == p[i + 1][1] and p[i - 1][1] == p[i][1]:
            answer += min(p[i + 1][0] - p[i][0], p[i][0] - p[i - 1][0])
        elif p[i][1] == p[i + 1][1]:
            answer += p[i + 1][0] - p[i][0]
        elif p[i - 1][1] == p[i][1]:
            answer += p[i][0] - p[i - 1][0]

print(answer)
