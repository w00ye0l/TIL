n1, n2 = map(int, input().split())

ant1 = list(input())
ant2 = list(input())

order = []
for i in range(n1 - 1, -1, -1):
    order.append((ant1[i], 0))

for i in range(n2):
    order.append((ant2[i], 1))

t = int(input())

for _ in range(t):
    i = 0
    while i < n1 + n2 - 1:
        if order[i][1] == 0 and order[i + 1][1] == 1:
            order[i], order[i + 1] = order[i + 1], order[i]
            i += 1
        i += 1

for i in range(n1 + n2):
    print(order[i][0], end="")
