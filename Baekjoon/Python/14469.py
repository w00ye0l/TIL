N = int(input())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort()

t = 0

for i in range(N):
    if t < arr[i][0]:
        t = arr[i][0]

    t += arr[i][1]

print(t)
