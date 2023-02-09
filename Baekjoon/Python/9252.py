arr1 = list(input())
arr2 = list(input())

dp = [[0 for _ in range(len(arr2) + 1)] for _ in range(len(arr1) + 1)]

for i in range(1, len(arr1) + 1):
    for j in range(1, len(arr2) + 1):
        if arr1[i - 1] == arr2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

result = []

i, j = len(arr1), len(arr2)

while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        result.append(arr1[i - 1])
        i -= 1
        j -= 1


if result:
    result.reverse()

    print(len(result))
    print("".join(result))
else:
    print(0)
