import sys

input = sys.stdin.readline

N = int(input())
arr = input()
answer = 0
temp = ""

for a in arr:
    if a.isdigit():
        temp += a
    else:
        answer += int(temp)
        temp = ""

print(answer - (N - 1) * N // 2)
