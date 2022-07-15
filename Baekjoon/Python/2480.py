a = list(map(int, input().split()))

a.sort()

if a[0] == a[1] and a[1] == a[2]:
    print(10000 + a[0] * 1000)
elif a[0] == a[1] and a[1] != a[2]:
    print(1000 + a[0] * 100)
elif a[0] != a[1] and a[1] == a[2]:
    print(1000 + a[1] * 100)
else:
    print(a[-1]*100)
