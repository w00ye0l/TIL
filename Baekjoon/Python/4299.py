sum_, sub_ = map(int, input().split())

if (sum_ + sub_) % 2 or (sum_ - sub_) < 0:
    print(-1)
else:
    result = [(sum_ + sub_) // 2, (sum_ - sub_) // 2]

    print(*sorted(result, reverse=True))
