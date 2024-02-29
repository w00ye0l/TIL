from collections import defaultdict

for _ in range(int(input())):
    W = input()
    K = int(input())
    dic = defaultdict(list)
    min_, max_ = float("inf"), 0

    for idx, char in enumerate(W):
        dic[char].append(idx)

    for char, arr in dic.items():
        if len(arr) >= K:
            for i in range(len(arr) - K + 1):
                l = arr[i + K - 1] - arr[i] + 1

                min_ = min(min_, l)
                max_ = max(max_, l)
        else:
            continue

    if min_ == float("inf") and max_ == 0:
        print(-1)
    else:
        print(min_, max_)
