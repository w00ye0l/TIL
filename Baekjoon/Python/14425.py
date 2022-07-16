n, m = map(int, input().split())
n_arr = []

for i in range(n):
    s = input().split()
    n_arr.append(s)

cnt = 0

for j in range(m):
    s = input().split()
    if s in n_arr:
        cnt += 1

print(cnt)
