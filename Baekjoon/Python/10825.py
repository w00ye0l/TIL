import sys
input = sys.stdin.readline

n = int(input())

scores = {}
for _ in range(n):
    temp = list(input().split())

    scores[temp[0]] = list(map(int, temp[1:4]))

scores = sorted(scores.items(), key=lambda x: (
    -x[1][0], x[1][1], -x[1][2], x[0]))

for i in range(n):
    print(scores[i][0])
