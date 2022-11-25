from pprint import pprint

a = input()
b = input()

ans = 0

arr = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
            ans = max(ans, arr[i][j])

pprint(ans)
