N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0

for i in range(N):
    if A[i] <= B[i]:
        answer += 1

print(answer)