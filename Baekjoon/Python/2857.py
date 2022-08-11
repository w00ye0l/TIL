fbi_list = []

for i in range(5):
    name = list(input().split('-'))
    for n in name:
        if 'FBI' in n:
            fbi_list.append(i + 1)

if not fbi_list:
    print('HE GOT AWAY!')
else:
    print(*fbi_list)
