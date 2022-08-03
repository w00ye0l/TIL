n = int(input())
sum_ = 0
name = set()

for _ in range(n):
    s = input()

    if s == 'ENTER':
        name.clear()
    else:
        if s not in name:
            name.add(s)
            sum_ += 1

print(sum_)
