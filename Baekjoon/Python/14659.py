n = int(input())

mountain = list(map(int, input().split()))

max_ = 0
result = 0

for i in range(n):
    if mountain[i] > max_:
        max_ = mountain[i]
        cnt = 0
    else:
        cnt += 1

    result = max(result, cnt)
    print(mountain, max_, result)

print(result)
