import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    five = 5
    answer = 0

    while True:
        if five > N:
            break

        answer += N // five
        five *= 5

    print(answer)
