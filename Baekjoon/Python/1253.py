n = int(input())

num = list(map(int, input().split()))

num.sort()

cnt = 0
for i in range(n):
    start = 0
    end = n - 1

    while start < end:
        if end == i:
            end -= 1
            continue

        if start == i:
            start += 1
            continue

        if num[start] + num[end] > num[i]:
            end -= 1

        elif num[start] + num[end] < num[i]:
            start += 1

        else:
            cnt += 1
            break

print(cnt)
