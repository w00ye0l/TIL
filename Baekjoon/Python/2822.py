dic = {}
arr = []
sum = 0

for i in range(8):
    n = int(input())
    dic[i] = n

dic = list(sorted(dic.items(), key=lambda x: x[1], reverse=True))

for i in range(5):
    arr.append(dic[i][0] + 1)
    sum += dic[i][1]

arr = list(map(str, sorted(arr)))

print(sum)
print(' '.join(arr))
