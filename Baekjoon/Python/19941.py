N, K = map(int, input().split())
arr = list(input())

answer = 0

for i in range(N):
    if arr[i] == "P":
        for j in range(i - K, i + K + 1):
            if -1 < j < N and arr[j] == "H":
                arr[j] = "."
                answer += 1
                break

print(answer)
