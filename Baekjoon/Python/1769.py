x = list(map(int, input()))

cnt = 0

while len(x) != 1:
    sum_ = sum(x)
    x = list(map(int, str(sum_)))
    cnt += 1

print(cnt)
if sum(x) % 3 == 0:
    print('YES')
else:
    print('NO')
