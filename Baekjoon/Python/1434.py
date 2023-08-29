N, M = map(int, input().split())

box = list(map(int, input().split()))
book = list(map(int, input().split()))

for i in range(M):
    for j in range(N):
        if box[j] >= book[i]:
            box[j] -= book[i]
            break

print(sum(box))
