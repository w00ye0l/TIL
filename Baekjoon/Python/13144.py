N = int(input())

arr = list(map(int, input().split()))

visited = [0 for _ in range(max(arr) + 1)]
answer = 0
e = 0

for i in range(N):
    while e < N:
        if visited[arr[e]]:
            break
        visited[arr[e]] = 1
        e += 1

    answer += e - i
    visited[arr[i]] = 0

print(answer)
