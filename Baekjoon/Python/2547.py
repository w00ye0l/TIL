import sys

input = sys.stdin.readline

for _ in range(int(input())):
    temp = input()

    N = int(input())

    cnt = 0

    for _ in range(N):
        cnt += int(input())

    if cnt % N == 0:
        print("YES")
    else:
        print("NO")
