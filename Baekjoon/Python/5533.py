n = int(input())

card = [list(map(int, input().split())) for _ in range(n)]
r_card = []
score = [0 for _ in range(n)]


for i in range(3):
    s = []
    for j in range(n):
        s.append(card[j][i])
    r_card.append(s)

for i in range(3):
    for j in range(n):
        if r_card[i].count(r_card[i][j]) == 1:
            score[j] += r_card[i][j]

for i in range(n):
    print(score[i])
