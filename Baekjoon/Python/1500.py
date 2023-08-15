S, K = map(int, input().split())

arr = [1 for _ in range(K)]
cnt = K
answer = 1

while cnt < S:
    arr[cnt % K] += 1
    cnt += 1

for a in arr:
    answer *= a

print(answer)
