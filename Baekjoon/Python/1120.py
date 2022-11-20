a, b = input().split()

if len(a) == len(b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1

    print(cnt)
else:
    gap_l = abs(len(a) - len(b))
    result = []
    if len(a) > len(b):
        l = len(b)
        for i in range(gap_l + 1):
            cnt = 0
            for j in range(l):
                if a[j + i] != b[j]:
                    cnt += 1
            result.append(cnt)
        answer = min(result)
    else:
        l = len(a)
        for i in range(gap_l + 1):
            cnt = 0
            for j in range(l):
                if a[j] != b[j + i]:
                    cnt += 1
            result.append(cnt)
        answer = min(result)

    print(answer)
