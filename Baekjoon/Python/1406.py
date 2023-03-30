import sys

input = sys.stdin.readline

arr = list(input().rstrip())
back = []

m = int(input())

for _ in range(m):
    order = list(input().split())

    if order[0] == "L":
        if arr:
            back.append(arr.pop())

    elif order[0] == "D":
        if back:
            arr.append(back.pop())

    elif order[0] == "B":
        if arr:
            arr.pop()

    elif order[0] == "P":
        arr.append(order[1])

print("".join(arr), "".join(reversed(back)), sep="")
