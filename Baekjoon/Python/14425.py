n, m = map(int, input().split())
n_arr = []
m_arr = []

for i in range(n):
    n_arr[i] = input()

for j in range(m):
    n_arr[j] = input()

min = n if n <= m else m
cnt = 0

for k in range(min):
    if n_arr[i] == m_arr[i]:
        cnt += 1

print(cnt)
