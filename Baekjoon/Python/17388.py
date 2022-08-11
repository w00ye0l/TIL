uni = ['Soongsil', 'Korea', 'Hanyang']

num = list(map(int, input().split()))

if sum(num) >= 100:
    print('OK')
else:
    print(uni[num.index(min(num))])
