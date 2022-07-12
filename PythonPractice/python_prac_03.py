# 1) while문
n = int(input())
x = 0
sum = 0
while x < n:
    x += 1
    sum += x
print(sum)

# 2) for문
n = int(input())
x = 0
sum = 0
for x in range(n):
    x += 1
    sum += x
print(sum)
