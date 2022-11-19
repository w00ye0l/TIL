import sys

input = sys.stdin.readline

for _ in range(3):
    n = int(input())

    sum_ = 0
    for i in range(n):
        sum_ += int(input())

    if sum_ == 0:
        print(0)
    elif sum_ > 0:
        print("+")
    else:
        print("-")
