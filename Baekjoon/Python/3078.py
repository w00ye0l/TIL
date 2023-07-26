import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [len(input().rstrip()) for _ in range(N)]

answer = 0
dic = defaultdict(int)

for i in range(N):
    if i > K:
        dic[arr[i - K - 1]] -= 1

    answer += dic[arr[i]]
    dic[arr[i]] += 1

print(answer)
