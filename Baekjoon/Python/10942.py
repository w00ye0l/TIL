# import sys

# input = sys.stdin.readline

# n = int(input())

# arr = list(map(int, input().split()))

# pel = [[0 for _ in range(n)] for _ in range(n)]

# for i in range(n):
#     pel[i][i] = 1

# for i in range(n - 1):
#     if arr[i] == arr[i + 1]:
#         pel[i][i + 1] = 1

# for i in range(2, n):
#     for j in range(n - i):
#         if arr[j] == arr[j + i] and pel[j + 1][j + i - 1]:
#             pel[j][j + i] = 1

# m = int(input())

# for _ in range(m):
#     s, e = map(int, input().split())

#     print(pel[s - 1][e - 1])


import sys

input = sys.stdin.readline


def pelCheck(start, end):
    while start > -1 and end < n:
        if arr[start] == arr[end]:
            pel[start][end] = 1
        else:
            break

        start -= 1
        end += 1


n = int(input())

arr = list(map(int, input().split()))

pel = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    pelCheck(i, i)
    pelCheck(i, i + 1)

m = int(input())

for _ in range(m):
    s, e = map(int, input().split())

    print(pel[s - 1][e - 1])
