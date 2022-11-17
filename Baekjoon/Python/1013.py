import re

n = int(input())

for _ in range(n):
    arr = input()

    chk = re.compile("(100+1+|01)+")

    if chk.fullmatch(arr):
        print("YES")
    else:
        print("NO")
