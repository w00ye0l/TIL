n = int(input())

arr = list(map(int, input().split()))

cnt = [[0, 0] for _ in range(n)]

for i in range(n):
    plus = arr[i] - 1
    minus = not plus

    cnt[i][plus] = cnt[i - 1][plus] + 1
    cnt[i][minus] = max(0, cnt[i - 1][minus] - 1)

print(max(map(max, cnt)))
