k = int(input())
d1, d2 = map(int, input().split())

print(pow(k, 2) - pow((d2 - d1) / 2, 2))
