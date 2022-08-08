n, m = map(int, input().split())

card = list(map(int, input().split()))
max_ = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum_ = card[i] + card[j] + card[k]

            if max_ < sum_ <= m:
                max_ = sum_

print(max_)
