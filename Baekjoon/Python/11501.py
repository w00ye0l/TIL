import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    price = list(map(int, input().split()))

    max_, answer = 0, 0

    for i in range(N - 1, -1, -1):
        if price[i] < max_:
            answer += max_ - price[i]
        else:
            max_ = price[i]

    print(answer)
