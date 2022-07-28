cnt = {}
result = []

n = int(input())

for i in range(n):
    card = int(input())
    if card not in cnt:
        cnt[card] = 1
    else:
        cnt[card] += 1

result = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

print(result[0][0])
