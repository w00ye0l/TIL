N = int(input())

score = list(map(int, input().split()))
new_score = [0] * N
s = 0

for i in range(N):
    if score[i]:
        s += score[i]
    else:
        s = 0

    new_score[i] = s

print(sum(new_score))
