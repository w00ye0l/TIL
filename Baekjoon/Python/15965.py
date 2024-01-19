K = int(input())
arr = [1 for _ in range(10**7 + 1)]
answer = []

for i in range(2, 10**7 + 1):
    if arr[i]:
        answer.append(i)
        for j in range(i * 2, 10**7 + 1, i):
            arr[j] = 0

print(answer[K - 1])
