from itertools import product

n = int(input())


light = []
for _ in range(5):
    light.append(list(input()))

num = {
    0: ("###", "#.#", "#.#", "#.#", "###"),
    1: ("..#", "..#", "..#", "..#", "..#"),
    2: ("###", "..#", "###", "#..", "###"),
    3: ("###", "..#", "###", "..#", "###"),
    4: ("#.#", "#.#", "###", "..#", "..#"),
    5: ("###", "#..", "###", "..#", "###"),
    6: ("###", "#..", "###", "#.#", "###"),
    7: ("###", "..#", "..#", "..#", "..#"),
    8: ("###", "#.#", "###", "#.#", "###"),
    9: ("###", "#.#", "###", "..#", "###"),
}

temp = [[] for _ in range(n)]


def check(i, l):
    for j in range(5):
        for k in range(3):
            if light[j][i + k] == "#" and num[l][j][k] == ".":
                return 0

    return 1


def solution(n):
    cnt = 0

    for i in range(0, 4 * n - 1, 4):
        for l in range(10):
            if check(i, l):
                temp[cnt].append(l)
        cnt += 1

    total, result = 1, []

    for i, e in enumerate(temp):
        total *= len(e)
        s = sum(e)
        result.append([s * 10 ** (n - i - 1), len(e)])

    if not total:
        print(-1)
        return

    s = 0
    for e in result:
        s += e[0] * total // e[1]

    print(s / total)


solution(n)
