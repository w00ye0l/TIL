n = int(input())

result = []
for _ in range(n):
    num = list(map(int, input().split()))

    temp = set(num)

    if len(temp) == 1:
        result.append(num[0] * 1000 + 10000)
    elif len(temp) == 2:
        for i in range(3):
            if num.count(num[i]) == 2:
                result.append(num[i] * 100 + 1000)
                break
    else:
        result.append(max(num) * 100)

print(max(result))
