n = int(input())
sum = 0

for x in range(1001):
    sum += x
    if n <= sum:
        break
print(x)
