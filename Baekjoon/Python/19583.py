import sys

input = sys.stdin.readline

s, e, q = input().split()

s = int(s[:2] + s[3:])
e = int(e[:2] + e[3:])
q = int(q[:2] + q[3:])

dic = {}
while True:
    try:
        t, name = input().split()
        t = int(t[:2] + t[3:])

        if t <= s:
            dic[name] = 1
        elif e <= t <= q and name in dic:
            dic[name] = 0
    except:
        break

print(list(dic.values()).count(0))
