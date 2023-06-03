N = int(input())

answer = float("inf")

for _ in range(N):
    A, B = map(int, input().split())

    if A <= B:
        answer = min(answer, B)

if answer != float("inf"):
    print(answer)
else:
    print(-1)
