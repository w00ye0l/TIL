n = int(input())

for _ in range(n):
    num = list(map(int, input().split()))

    num.sort()

    print(num[-3])
