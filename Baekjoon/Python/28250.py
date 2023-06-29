N = int(input())
arr = list(map(int, input().split()))
temp = [0] * 3

for i in range(N):
    if arr[i] < 2:
        temp[arr[i]] += 1
    else:
        temp[2] += 1

answer = 2 * temp[0] * temp[1] + temp[0] * (temp[0] - 1) // 2 + temp[0] * temp[2]
print(answer)
