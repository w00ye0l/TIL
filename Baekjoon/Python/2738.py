n, m = map(int, input().split())

arr1 = []
for i in range(n):
    arr1.append(list(map(int, input().split())))

arr2 = []
for i in range(n):
    arr2.append(list(map(int, input().split())))

result = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(arr1[i][j] + arr2[i][j])
    result.append(temp)

for i in range(n):
    for j in range(m):
        print(result[i][j], end=" ")
    print()
