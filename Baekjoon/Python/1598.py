a, b = map(int, input().split())

a_i, a_j = (4 if a % 4 == 0 else a % 4), (a // 4 if a % 4 == 0 else a // 4 + 1)
b_i, b_j = (4 if b % 4 == 0 else b % 4), (b // 4 if b % 4 == 0 else b // 4 + 1)

print(abs(a_i - b_i) + abs(a_j - b_j))
