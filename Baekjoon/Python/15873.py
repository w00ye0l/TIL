num = int(input())

if num <= 109:
    a = num // 10
    b = num % 10
else:
    a = num // 100
    b = num % 100

print(a + b)
