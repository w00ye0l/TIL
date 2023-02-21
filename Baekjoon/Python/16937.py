def check(r1, c1, r2, c2):
    global maxArea

    if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
        maxArea = max(maxArea, r1 * c1 + r2 * c2)


h, w = map(int, input().split())
n = int(input())

paper = [[0 for _ in range(w)] for _ in range(h)]
sticker = []

for _ in range(n):
    sticker.append(tuple(map(int, input().split())))

maxArea = 0

for i in range(n):
    for j in range(i + 1, n):
        r1, c1 = sticker[i]
        r2, c2 = sticker[j]

        check(r1, c1, r2, c2)
        check(c1, r1, r2, c2)
        check(r1, c1, c2, r2)
        check(c1, r1, c2, r2)

print(maxArea)
