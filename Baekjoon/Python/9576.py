import sys

input = sys.stdin.readline


for _ in range(int(input())):
    N, M = map(int, input().split())

    books = [0] * (N + 1)
    wants = []

    for _ in range(M):
        a, b = map(int, input().split())
        wants.append((a, b))

    wants.sort(key=lambda x: x[1])

    for a, b in wants:
        for i in range(a, b + 1):
            if books[i]:
                continue

            books[i] = 1
            break

    print(sum(books))
