import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}

for _ in range(n):
    word = input().rstrip()

    if len(word) < m:
        continue

    if not word in dic:
        dic[word] = [1, len(word)]
    else:
        dic[word][0] += 1

print(*sorted(dic.keys(), key=lambda x: (-dic[x][0], -dic[x][1], x)), sep="\n")
