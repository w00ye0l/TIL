result = [int(i) for i in range(1, 10001)]

for i in range(1, 10001):
    arr = list(map(int, str(i)))
    sum_ = i + sum(arr)

    if sum_ in result:
        result.remove(sum_)

for i in result:
    print(i)
