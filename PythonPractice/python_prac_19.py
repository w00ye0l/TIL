number = int(input())
cnt = 0

while number > 0:
    number //= 10
    cnt += 1

print(cnt)
