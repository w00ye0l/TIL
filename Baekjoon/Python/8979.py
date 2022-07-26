n, k = map(int, input().split())
arr = []
rank = 0

for i in range(n):
    s = list(map(int, input().split()))
    arr.append(s)
    if arr[i][0] == k:
        idx = i

for i in range(n):
    if i != idx:
        if arr[i][1] > arr[idx][1]:
            rank += 1
        elif arr[i][1] == arr[idx][1]:
            if arr[i][2] > arr[idx][2]:
                rank += 1
            elif arr[i][2] == arr[idx][2]:
                if arr[i][3] > arr[idx][3]:
                    rank += 1

print(rank + 1)
