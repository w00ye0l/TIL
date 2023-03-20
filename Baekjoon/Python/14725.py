n = int(input())
result = []

for _ in range(n):
    temp = list(input().split())
    result.append(temp[1:])

result.sort()

for i in range(n):
    cnt = 0
    if i != 0:
        for j in range(len(result[i])):
            if len(result[i - 1]) <= j or result[i - 1][j] != result[i][j]:
                break
            else:
                cnt = j + 1

    for j in range(cnt, len(result[i])):
        print("--" * j + result[i][j])
