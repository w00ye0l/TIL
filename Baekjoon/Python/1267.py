N = int(input())
arr = list(map(int, input().split()))

ys, ms = 0, 0

for i in range(N):
    ys += (arr[i] // 30 + 1) * 10
    ms += (arr[i] // 60 + 1) * 15

if ys > ms:
    print(f"M {ms}")
elif ys < ms:
    print(f"Y {ys}")
else:
    print(f"Y M {ys}")
