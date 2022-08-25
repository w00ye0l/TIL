from collections import deque

l = int(input())
answer = list(map(int, input().split()))
n = int(input())

result = []
for _ in range(n):
    sign = False
    chk = list(map(int, input().split()))

    temp = deque(chk)

    for i in range(l):
        p = temp.popleft()
        temp.append(p)

        if list(temp) == answer:
            sign = True
            result.append(chk)
            break

    if sign == True:
        continue

    temp = deque(chk[::-1])
    for i in range(l):
        temp[i] -= 2

        if temp[i] <= 0:
            temp[i] += 4

    for i in range(l):
        p = temp.popleft()
        temp.append(p)

        if list(temp) == answer:
            sign = True
            result.append(chk)
            break

print(len(result))
for r in result:
    print(*r)
