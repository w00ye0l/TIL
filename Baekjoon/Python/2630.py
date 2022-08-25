w_p, b_p = 0, 0


def paper_cnt(s_x, s_y, n):
    global w_p, b_p
    cnt = 0
    for i in range(s_x, s_x + n):
        for j in range(s_y, s_y + n):
            if paper[i][j] == 1:
                cnt += 1

    if cnt == n ** 2:
        b_p += 1
        return
    elif cnt == 0:
        w_p += 1
        return

    paper_cnt(s_x, s_y, n//2)
    paper_cnt(s_x + n//2, s_y, n//2)
    paper_cnt(s_x, s_y + n//2, n//2)
    paper_cnt(s_x + n//2, s_y + n//2, n//2)


n = int(input())

paper = []
cnt = 0
for _ in range(n):
    p = list(map(int, input().split()))
    paper.append(p)

paper_cnt(0, 0, n)

print(w_p)
print(b_p)
