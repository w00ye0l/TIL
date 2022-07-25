n = int(input())

arr = list(map(int, input().split()))
arr = sorted(list(set(arr)))

for i in arr:
    print(i, end=' ')
