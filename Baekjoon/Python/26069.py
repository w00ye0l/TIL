n = int(input())

dance = set()
dance.add("ChongChong")

for _ in range(n):
    a, b = input().split()

    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)

print(len(dance))
