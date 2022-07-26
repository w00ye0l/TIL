n = int(input())
arr = [str(i) for i in range(1, n + 1)]
result = []

for i in range(n):
    p = arr.pop(0)
    result.append(p)

    if arr:
        pp = arr.pop(0)
        arr.append(pp)

print(' '.join(result))
