x = int(input())

n = int(input())

sum_ = 0
for _ in range(n):
    a, b = map(int, input().split())
    sum_ += a * b

if sum_ == x:
    print('Yes')
else:
    print('No')
