N = int(input())
arr = [input() for _ in range(N)]
chk = [0] * N

arr.sort()

for i in range(N - 1):
    if arr[i + 1].startswith(arr[i]):
        chk[i] += 1

print(chk.count(0))
