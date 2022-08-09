n = int(input())

for i in range(n, 0, -1):
    temp = str(i)
    temp = temp.replace('4', '')
    temp = temp.replace('7', '')

    if temp == '':
        print(i)
        break
