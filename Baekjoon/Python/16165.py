N, M = map(int, input().split())

group = {}

for _ in range(N):
    team = input()
    num = int(input())
    member = [input() for _ in range(num)]
    member.sort()

    group[team] = member

for _ in range(M):
    name = input()
    t = int(input())

    if t == 1:
        for k, v in group.items():
            if name in v:
                print(k)
                break
    else:
        for k, v in group.items():
            if name == k:
                for i in v:
                    print(i)
                break
