n, m = map(int, input().split())
arr = []
result = ""
cnt = 0

for i in range(n):
    arr.append(input())

for i in range(m):
    dic = {}

    for j in range(n):
        if arr[j][i] not in dic:
            dic[arr[j][i]] = 1
        else:
            dic[arr[j][i]] += 1

    s_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    result += s_dic[0][0]

print(result)

for i in range(n):
    for j in range(m):
        if arr[i][j] != result[j]:
            cnt += 1

print(cnt)
