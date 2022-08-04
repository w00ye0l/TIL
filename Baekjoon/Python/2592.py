sum_ = 0
num = {}

for _ in range(10):
    n = int(input())

    if n not in num:
        num[n] = 1
    else:
        num[n] += 1

    sum_ += n

num = sorted(num.items(), key=lambda x: (-x[1], x[0]))

print(sum_//10)
print(num[0][0])
