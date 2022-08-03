n, m = map(int, input().split())

guard = [list(input()) for _ in range(n)]
r_cnt = 0
c_cnt = 0

for i in range(n):
    if 'X' not in guard[i]:
        r_cnt += 1

for i in range(m):
    c_check = False
    for j in range(n):
        if guard[j][i] == 'X':
            c_check = True
    if c_check == False:
        c_cnt += 1

print(r_cnt if r_cnt > c_cnt else c_cnt)
