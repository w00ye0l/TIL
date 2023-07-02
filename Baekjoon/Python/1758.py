import sys

input = sys.stdin.readline

N = int(input())
money = [int(input()) for _ in range(N)]

money.sort(reverse=True)

answer = 0

for i in range(N):
    answer += max(0, money[i] - i)

print(answer)
