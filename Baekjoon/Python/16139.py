import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())

cnt = [[0]*26]
cnt[0][ord(s[0]) - ord('a')] = 1

for i in range(1, len(s)):
    cnt.append(cnt[-1][:])
    cnt[i][ord(s[i]) - ord('a')] += 1

for _ in range(q):
    alpha, l, r = list(input().split())
    l, r = int(l), int(r)

    if l == 0:
        print(cnt[r][ord(alpha) - ord('a')])
    else:
        print(cnt[r][ord(alpha) - ord('a')] -
              cnt[l - 1][ord(alpha) - ord('a')])
