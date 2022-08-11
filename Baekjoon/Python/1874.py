n = int(input())

check = [0]
for i in range(n):
    check.append(int(input()))

pnp = []
result = [0]
stack = []
i = 1

for j in range(1, n + 1):
    stack.append(j)
    pnp.append('+')

    while stack:
        num = stack.pop()
        if num == check[i]:
            result.append(num)
            pnp.append('-')
            i += 1
        else:
            stack.append(num)
            break

if len(check) == len(result):
    for p in pnp:
        print(p)
else:
    print('NO')
