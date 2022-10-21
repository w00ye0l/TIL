import sys

N, K = map(int, sys.stdin.readline().split())
bag = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())

    if W > K:
        continue

    for i in range(K, 0, -1):
        if bag[i] > 0 and i + W <= K:
            bag[i + W] = max(bag[i + W], bag[i] + V)

    bag[W] = max(bag[W], V)

print(max(bag))

# n, k = map(int, input().split())

# thing = [[0, 0]]
# d = [[0] * (k + 1) for _ in range(n + 1)]

# for i in range(n):
#     thing.append(list(map(int, input().split())))

# for i in range(1, n + 1):
#     for j in range(1, k + 1):
#         w = thing[i][0]
#         v = thing[i][1]

#         if j < w:
#             d[i][j] = d[i - 1][j]
#         else:
#             d[i][j] = max(d[i - 1][j], d[i - 1][j - w] + v)

# print(d[n][k])
