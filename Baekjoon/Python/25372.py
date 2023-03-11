import sys

input = sys.stdin.readline

for _ in range(int(input())):
    arr = input().rstrip()

    if 6 <= len(arr) <= 9:
        print("yes")
    else:
        print("no")
