N = int(input())
# area, height, weight, index
arr = [[0, 0, 0, 0]]
for i in range(N):
    arr.append(list(map(int, input().split())) + [i + 1])

arr.sort(key=lambda x: x[2])
dp = [0] * (N + 1)
dis = [-1] * (N + 1)
answer = []
maxHeight, maxIdx = 0, 0

for i in range(1, N + 1):
    for j in range(i - 1, -1, -1):
        if arr[i][0] > arr[j][0]:
            if dp[i] < dp[j] + arr[i][1]:
                dp[i] = dp[j] + arr[i][1]
                dis[i] = j

    if maxHeight < dp[i]:
        maxHeight = dp[i]
        maxIdx = i

while True:
    if maxIdx != 0:
        answer.append(arr[maxIdx][3])
        maxIdx = dis[maxIdx]
    else:
        break

print(len(answer))
while answer:
    print(answer.pop())
