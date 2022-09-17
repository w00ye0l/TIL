n = int(input())

sirial = {}
for _ in range(n):
    temp = list(input())
    len_ = len(temp)

    sum_ = 0
    for t in temp:
        if ord(t) < ord('A'):
            sum_ += int(t)

    sirial[''.join(temp)] = [len_, sum_]

sirial = sorted(sirial.items(), key=lambda x: (x[1][0], x[1][1], x[0]))

for s in sirial:
    print(s[0])
