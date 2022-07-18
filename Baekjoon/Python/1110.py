n = int(input())
x = n
cnt = 0

while True:
    n = ((n % 10) * 10) + (((n // 10) + (n % 10)) % 10)
    cnt += 1
    if x == n:
        break

print(cnt)
