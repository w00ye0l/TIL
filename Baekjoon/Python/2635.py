n = int(input())

temp = [n]
len_list = []
result = []

for i in range(n // 2 + 1, n + 1):
    temp.append(i)

    j = 0
    while True:
        if temp[j] - temp[j + 1] >= 0:
            temp.append(temp[j] - temp[j + 1])
        else:
            len_list.append(len(temp))
            result.append(temp)
            break
        j += 1

    temp = [n]

print(max(len_list))
print(*result[len_list.index(max(len_list))])
