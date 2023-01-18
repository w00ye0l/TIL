n, k = map(int, input().split())

stack_ = []
stack_.append((n, ""))

result = []
while stack_:
    (cur, temp) = stack_.pop()

    if cur == 0:
        result.append(temp)
        continue

    for i in range(1, 4):
        if cur >= i:
            stack_.append((cur - i, temp + str(i)))

result.sort()

if k <= len(result):
    print("+".join(list(result[k - 1])))
else:
    print(-1)
