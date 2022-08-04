g = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())
    grade = []

    for j in range(10):
        for l in range(n // 10):
            grade.append(g[j])

    score = {}

    for j in range(n):
        mid, final, hw = map(float, input().split())
        score[j + 1] = (mid * 0.35) + (final * 0.45) + (hw * 0.2)

    score = sorted(score.items(), key=lambda x: (-x[1], x[0]))

    idx = 0
    for j in range(n):
        if k == score[j][0]:
            idx = j

    print(f'#{i} {grade[idx]}')
