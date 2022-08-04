n, m = map(int, input().split())

bread = []

for _ in range(n):
    bread.append(input()[::-1])

print(*bread, sep="\n")
