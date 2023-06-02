N = int(input())

times = list(map(int, input().split()))

total = sum(times) + 8 * (N - 1)
day = total // 24
hour = total % 24

print(day, hour)
