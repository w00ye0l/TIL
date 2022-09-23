import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

m_cnt, z_cnt, p_cnt = 0, 0, 0


def chk(s1, s2, n):
    global m_cnt, z_cnt, p_cnt
    num = paper[s1][s2]

    for i in range(s1, s1 + n):
        for j in range(s2, s2 + n):
            if paper[i][j] != num:
                for a in range(3):
                    for b in range(3):
                        chk((s1 + (n // 3) * a), (s2 + (n // 3) * b), n // 3)
                return

    if num == -1:
        m_cnt += 1
    elif num == 0:
        z_cnt += 1
    elif num == 1:
        p_cnt += 1


n = int(input())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

chk(0, 0, n)

print(m_cnt)
print(z_cnt)
print(p_cnt)
