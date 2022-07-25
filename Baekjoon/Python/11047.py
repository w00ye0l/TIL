n, k = map(int, input().split())
arr = []
cnt = 0

for i in range(n):
    s = int(input())
    arr.append(s)

arr.sort(reverse=True)

for i in arr:
    if i <= k:
        cnt += k // i
        k %= i

print(cnt)
