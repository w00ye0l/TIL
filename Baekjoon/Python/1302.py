n = int(input())

count_dic = {}
result = []

for i in range(n):
    s = input()
    if s not in count_dic:
        count_dic[s] = 1
    else:
        count_dic[s] += 1

count_dic = sorted(count_dic.items(), key=lambda x: x[1])

for i in count_dic:
    if count_dic[-1][1] == i[1]:
        result.append(i[0])

result.sort()

print(result[0])
