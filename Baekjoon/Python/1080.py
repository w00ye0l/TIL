def reverseMatrix(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if A[i][j] == "0":
                A[i][j] = "1"
            else:
                A[i][j] = "0"


N, M = map(int, input().split())

A, B = [], []

for _ in range(N):
    A.append(list(input()))

for _ in range(N):
    B.append(list(input()))

answer = 0

if (N < 3 or M < 3) and A != B:
    print(-1)
else:
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                reverseMatrix(i, j)
                answer += 1

    if A == B:
        print(answer)
    else:
        print(-1)
