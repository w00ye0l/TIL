N = int(input())

arr = []

for _ in range(N):
    L, H = map(int, input().split())

    arr.append((L, H))

arr.sort()

answer = 0
x, h = arr[0]

for i in range(1, N):
    if h <= arr[i][1]:
        answer += (arr[i][0] - x) * h

        x, h = arr[i]

x, h = arr[N - 1]

for i in range(N - 1, -1, -1):
    if h < arr[i][1]:
        answer += (x - arr[i][0]) * h

        x, h = arr[i]

answer += h

print(answer)
