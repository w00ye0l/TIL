n, k = map(int, input().split())

arr = [(i + 1) for i in range(n)]

t = k - 1
print(f"<{arr.pop(t)}", end="")

for i in range(n - 1):
    t += k - 1

    if t >= len(arr):
        t %= len(arr)

    print(f", {arr.pop(t)}", end="")

print(">")
