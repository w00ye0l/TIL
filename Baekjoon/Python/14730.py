N = int(input())

answer = 0

for _ in range(N):
    C, K = map(int, input().split())

    answer += C * K

print(answer)
