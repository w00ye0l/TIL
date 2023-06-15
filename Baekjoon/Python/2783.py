X, Y = map(int, input().split())
N = int(input())

cost = [1000 / Y * X]

for _ in range(N):
    Xi, Yi = map(int, input().split())
    cost.append(1000 / Yi * Xi)

cost.sort()

print(f"{cost[0]:.2f}")
