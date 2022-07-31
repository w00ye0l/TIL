l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.append(0)
s.sort()
result = 0

for i in range(len(s) - 1):
    if s[i] < n and n < s[i + 1]:
        small_cnt = n - s[i]
        big_cnt = s[i + 1] - n
        result = (small_cnt * big_cnt) - 1
        break

print(result)
