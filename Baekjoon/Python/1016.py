min_, max_ = map(int, input().split())

arr = [0 for _ in range(max_ - min_ + 1)]

cnt = max_ - min_ + 1
i = 2

while i**2 <= max_:
    j = min_ // (i**2)

    # 처음으로 나누어 떨어지는 제곱수를 구하기 위해
    if j * (i**2) < min_:
        j += 1

    while i**2 * j <= max_:
        if arr[i**2 * j - min_] == 0:
            arr[i**2 * j - min_] = 1
            cnt -= 1

        j += 1

    i += 1

print(cnt)
