import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[float("inf") if i != j else 0 for i in range(n)] for j in range(n)]
route = [[[i + 1] if i != j else [] for i in range(n)] for j in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a - 1][b - 1] = min(arr[a - 1][b - 1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
                    route[i][j] = route[i][k] + route[k][j]

for i in range(n):
    for j in range(n):
        if arr[i][j] != float("inf"):
            print(arr[i][j], end=" ")
        else:
            print(0, end=" ")
    print()

for i in range(n):
    for j in range(n):
        if not route[i][j] or arr[i][j] == float("inf"):
            print(0)
        else:
            print(len(route[i][j]) + 1, end=" ")
            print(i + 1, end=" ")
            print(*route[i][j])
