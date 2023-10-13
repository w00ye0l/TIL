import sys

input = sys.stdin.readline

while True:
    n = int(input())

    if n == -1:
        break

    c = []
    s = 0

    for i in range(1, n):
        if n % i == 0:
            c.append(i)
            s += i

    if s == n:
        cStr = " + ".join(list(map(str, c)))
        print(f"{n} = {cStr}")
    else:
        print(f"{n} is NOT perfect.")
