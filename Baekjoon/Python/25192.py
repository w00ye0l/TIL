n = int(input())
sum_ = 0
name = set()

for _ in range(n):
    s = input()

    if s == 'ENTER':
        sum_ += len(name)
        name = set()
    else:
        name.add(s)

sum_ += len(name)

print(sum_)
