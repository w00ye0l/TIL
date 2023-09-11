N = int(input())

arr = []

for _ in range(N):
    arr.append(input())

k = 1
l = len(arr[0])

while True:
    temp = set()

    for i in range(N):
        temp.add(arr[i][l - k : l])

    if len(temp) == N:
        print(k)
        break

    k += 1
