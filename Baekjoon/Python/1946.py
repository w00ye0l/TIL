import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    emp = []
    for i in range(n):
        emp.append(list(map(int, input().split())))

    emp.sort()

    comp = emp[0][1]
    cnt = 1

    for i in range(1, n):
        if comp > emp[i][1]:
            cnt += 1
            comp = emp[i][1]

    print(cnt)
