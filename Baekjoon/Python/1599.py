dic = {
    'a': 1,
    'b': 2,
    'k': 3,
    'd': 4,
    'e': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'l': 9,
    'm': 10,
    'n': 11,
    'x': 12,
    'o': 13,
    'p': 14,
    'r': 15,
    's': 16,
    't': 17,
    'u': 18,
    'w': 19,
    'y': 20
}

n = int(input())

temp = []
for _ in range(n):
    s = input()

    s = s.replace('ng', 'x')

    cnt = []
    for i in s:
        cnt.append(dic[i])

    temp.append([s, cnt])

temp.sort(key=lambda x: x[1])

for t in temp:
    t[0] = t[0].replace('x', 'ng')

    print(t[0])
