from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic = defaultdict(int)
s_arr = [0 for _ in range(n)]
cnt = 0

for i in range(n):
    s_arr[i] = s_arr[i - 1] + arr[i]

    if s_arr[i] == k:
        cnt += 1

    if s_arr[i] - k in dic:
        cnt += dic[s_arr[i] - k]

    dic[s_arr[i]] += 1

print(cnt)
