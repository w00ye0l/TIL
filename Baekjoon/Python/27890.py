x0, N = map(int, input().split())

for i in range(N):
    if x0 % 2:
        x0 = (x0 * 2) ^ 6
    else:
        x0 = int(x0 / 2) ^ 6

print(x0)