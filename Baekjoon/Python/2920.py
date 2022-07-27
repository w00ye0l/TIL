n = list(map(int, input().split()))
a = [i for i in range(1, 9)]
d = [i for i in range(8, 0, -1)]

if n == a:
    print('ascending')
elif n == d:
    print('descending')
else:
    print('mixed')
