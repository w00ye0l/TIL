n, m = map(int, input().split())
n_arr = []

for i in range(n):
    s = input()
    n_arr.append(s)

cnt = 0

for j in range(m):
    s = input()
    if s in set(n_arr):
        cnt += 1

print(cnt)
