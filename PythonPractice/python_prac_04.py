# 1) while문
n = int(input())
x = 1
result = 1
while(x <= n):
    result *= x
    x += 1
print(result)

# 2) for문
n = int(input())
x = 0
result = 1
for x in range(n):
    x += 1
    result *= x
print(result)
