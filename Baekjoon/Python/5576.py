w_score = []
k_score = []

for _ in range(10):
    w_score.append(int(input()))

for _ in range(10):
    k_score.append(int(input()))

w_score = sorted(w_score, reverse=True)[:3]
k_score = sorted(k_score, reverse=True)[:3]

print(sum(w_score), sum(k_score))
