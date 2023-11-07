def merge_sort(arr, p, r):
    if p < r and cnt <= K:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


def merge(arr, p, q, r):
    global cnt, result
    i, j = p, q + 1
    tmp = []

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= q:
        tmp.append(arr[i])
        i += 1

    while j <= r:
        tmp.append(arr[j])
        j += 1

    i, t = p, 0
    while i <= r:
        arr[i] = tmp[t]
        cnt += 1

        if cnt == K:
            result = arr[i]
            break

        i += 1
        t += 1


N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt, result = 0, -1

merge_sort(arr, 0, N - 1)

print(result)
