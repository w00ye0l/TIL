n = int(input())

tree = list(map(int, input().split()))
tree.sort(reverse=True)

day = []

for i in range(n):
    day.append(i + tree[i] + 2)

print(max(day))
