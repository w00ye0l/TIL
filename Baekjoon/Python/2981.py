import math

n = int(input())
arr = []
re = []
gcd = 0

for i in range(n):
    arr.append(int(input()))
    if i == 1:
        gcd = abs(arr[1] - arr[0])
    gcd = math.gcd(abs(arr[i] - arr[i - 1]), gcd)

for i in range(2, int(gcd**0.5) + 1):
    if gcd % i == 0:
        re.append(i)
        re.append(gcd // i)

re.append(gcd)
re = list(set(re))
re.sort()

for i in re:
    print(i, end=' ')
