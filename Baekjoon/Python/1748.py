n = input()

cnt = len(n)
n = int(n)

sum_ = 0

for i in range(cnt):
    if n - (10 ** i - 1) > 0:
        sum_ += n - (10 ** i - 1)

print(sum_)
