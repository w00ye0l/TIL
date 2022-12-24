n, m = map(int, input().split())

truth = set(list(map(int, input().split()))[1:])

party = []
for _ in range(m):
    party.append(set(list(map(int, input().split()))[1:]))

cnt = 0
while True:
    temp = 0
    for i in range(m):
        if len(truth & party[i]):
            truth = truth.union(party[i])
        else:
            temp += 1

    if cnt != temp:
        cnt = temp
    else:
        print(cnt)
        break
