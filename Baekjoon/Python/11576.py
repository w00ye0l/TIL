a, b = map(int, input().split())
m = int(input())
a_arr = list(map(int, input().split()))

temp = 0
result = []

for i in range(m):
    temp += a_arr[i] * (a ** (m - i - 1))

while temp:
    result.append(temp % b)
    temp //= b

print(*result[::-1])
