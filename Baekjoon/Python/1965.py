n = int(input())

box = list(map(int, input().split()))

cnt = []
cnt.append(1)

for i in range(1, n):
    d = []
    for j in range(i):
        if box[i] > box[j]:
            d.append(cnt[j] + 1)

    print(d)

    if not d:
        cnt.append(1)
    else:
        cnt.append(max(d))

print(max(cnt))
