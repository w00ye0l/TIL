N = int(input())
arr = list(map(int, input().split()))

answer = 0

for i in range(N):
    answer += 2
    answer += arr[i] * 4

    if i != 0:
        answer -= min(arr[i - 1], arr[i]) * 2

print(answer)
