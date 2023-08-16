import sys

input = sys.stdin.readline


def getScorePlus(arr):
    global answer

    if len(arr) % 2:
        answer += arr.pop()

    while arr:
        f = arr.pop()
        s = arr.pop()

        if f == 1 or s == 1:
            answer += f + s
        else:
            answer += f * s


def getScoreMinus(arr):
    global answer

    if len(arr) % 2:
        answer += arr.pop()

    while arr:
        answer += arr.pop() * arr.pop()


n = int(input())

plus = []
minus = []

for _ in range(n):
    num = int(input())

    if num > 0:
        plus.append(num)
    else:
        minus.append(num)

answer = 0

plus.sort(reverse=True)
minus.sort()

getScorePlus(plus)
getScoreMinus(minus)

print(answer)
