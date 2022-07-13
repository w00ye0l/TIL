n = int(input(), 16)

for i in range(1, 16):
    print(f'{n:X}*{i:X}={n*i:X}')
