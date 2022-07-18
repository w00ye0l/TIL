n = int(input())
arr = list(map(int, input().split()))

print(sum(arr) / n / max(arr) * 100)
