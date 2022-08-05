n = int(input())
f = int(input())

origin = n // 100
origin *= 100

for i in range(100):
    if (origin + i) % f == 0:
        print(f'{i:02d}')
        break
