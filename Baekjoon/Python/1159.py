from collections import defaultdict

n = int(input())

players = defaultdict(int)

for _ in range(n):
    name = input()
    players[name[0]] += 1

selection = []

for k, v in players.items():
    if v >= 5:
        selection.append(k)

selection.sort()

if selection:
    print("".join(selection))
else:
    print("PREDAJA")
