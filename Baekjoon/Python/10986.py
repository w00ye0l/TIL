import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [0] + list(map(int, input().split()))
mod_m = [0] * m

for i in range(1, n + 1):
    num[i] += num[i - 1]
    mod_m[num[i] % m] += 1

result = mod_m[0]

for c in mod_m:
    result += c * (c - 1) // 2

print(result)
