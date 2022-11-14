n = int(input())

arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    r, c = map(int, input().split())

    for i in range(r, r + 10):
        for j in range(c, c + 10):
            arr[i][j] = 1

sum_ = 0
for i in range(101):
    sum_ += arr[i].count(1)

print(sum_)
