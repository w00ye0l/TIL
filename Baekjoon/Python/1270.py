import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))

    dic = defaultdict(int)

    for a in arr[1:]:
        dic[a] += 1

    result = "SYJKGW"

    for k, v in dic.items():
        if v > (len(arr) - 1) // 2:
            result = str(k)

    print(result)
