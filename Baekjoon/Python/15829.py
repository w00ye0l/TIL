l = int(input())

arr = list(map(ord, list(input())))

sum_ = 0
for i in range(l):
    sum_ += (arr[i] - ord('a') + 1) * (31 ** i)

sum_ %= 1234567891

print(sum_)
